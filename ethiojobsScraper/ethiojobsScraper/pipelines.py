# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from sqlite3 import adapters
from itemadapter import ItemAdapter

from datetime import datetime


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
