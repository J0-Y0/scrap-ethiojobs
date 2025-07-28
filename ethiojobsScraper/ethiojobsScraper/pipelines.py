import psycopg2
import os

from sqlite3 import adapters
from itemadapter import ItemAdapter

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class EthiojobsscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # Clean up whitespaces in string fields
        for field in adapter.field_names():
            if isinstance(adapter.get(field), str):
                adapter[field] = adapter.get(field).strip()

        # convert deadline string to date
        if "deadline" in adapter.field_names():
            deadline = adapter.get("deadline")
            if deadline:
                # Assuming the deadline is in a format like: "August 5th, 2025 August 1st, 2025, August 2nd, 2025, August 3rd, 2025,July 31st, 2025 .....
                try:
                    month, day, year = deadline.split(" ")
                    # Handle the 'th', 'st', 'nd', 'rd' in day
                    day = "".join(filter(str.isdigit, day))  # Extract digits only
                    adapter["deadline"] = datetime.strptime(
                        f"{month} {day} {year}", "%B %d %Y"
                    ).date()
                except ValueError:
                    spider.logger.error(f"Invalid deadline format: {deadline}")
                    adapter["deadline"] = None
                    print("Invalid deadline format==:", deadline)
        return item


class SaveToPostgresDatabase:

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.create_connection()

    def create_connection(self):

        try:
            self.conn = psycopg2.connect(
                host=os.getenv("HOST", "localhost"),
                database=os.getenv("DATABASE"),
                user=os.getenv("USER"),
                password=os.getenv(
                    "PASSWORD",
                ),
            )
            self.cursor = self.conn.cursor()

            # create table jobs if not exists
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS jobs (
                    id SERIAL PRIMARY KEY,
                    title TEXT ,
                    company TEXT ,
                    location TEXT ,
                    deadline DATE,
                    about TEXT,
                    url TEXT UNIQUE
                );
            """
            )
            print("PostgreSQL connection established.")
        except Exception as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # Prepare the SQL query
        sql = """
            INSERT INTO jobs (title, company, location, deadline, about, url)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (url) DO NOTHING;
        """
        values = (
            adapter.get("title"),
            adapter.get("company"),
            adapter.get("location"),
            adapter.get("deadline"),
            adapter.get("about"),
            adapter.get("url"),
        )

        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print(f"Error inserting item into PostgreSQL: {e}")
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("PostgreSQL connection closed.")
