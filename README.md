# Ethiojobs Scraper

A professional Scrapy-based web scraper for extracting job listings from ethiojobs.net. This project utilizes Playwright for headless browsing and ScrapeOps for request headers management.

## Features
- **Job Data Extraction**: Scrapes title, company, description, location, deadline, and URL
- **Automatic Pagination**: Handles multi-page job listings automatically
- **Bot Detection Avoidance**: Uses rotating headers via ScrapeOps
- **Data Export**: Exports results to JSON format
- **Database Integration**: Saves job listings to PostgreSQL database
- **Data Cleaning Pipeline**:
  - Automatically strips whitespace from all text fields
  - Converts deadline strings to proper date formats
  - Handles invalid date formats gracefully
- **Database Management**:
  - Creates database table automatically if not exists
  - Prevents duplicate entries using URL uniqueness
  - Ensures proper connection handling

## Installation
1. Clone the repository:
```bash
git clone https://github.com/J0-Y0/scrap-ethiojobs.git
cd scrap-ethiojobs
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
Create a `.env` file in the project root with your ScrapeOps API key and PostgreSQL credentials:
```env
SCRAPEOPS_API_KEY=your_api_key_here
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT=http://headers.scrapeops.io/v1/user-agents
SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT=http://headers.scrapeops.io/v1/browser-headers

# PostgreSQL Configuration
DB_HOST=your_postgres_host
DB_PORT=5432
DB_NAME=ethiojobs
DB_USER=postgres_user
DB_PASSWORD=postgres_password
```

## Database Setup
1. Create PostgreSQL database and table:
```sql
CREATE DATABASE ethiojobs;
\c ethiojobs

CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title TEXT,
    company TEXT,
    about TEXT,
    location TEXT,
    deadline TEXT,
    url TEXT
);
```

2. Ensure the PostgreSQL server is running and accessible

## Usage
Run the spider with:
```bash
scrapy crawl ethiojobs -O output.json
```

This will:
1. Start scraping from the main jobs page
2. Follow pagination links
3. Extract job details
4. Save results to `output.json`
5. Save results to PostgreSQL database

## Data Structure
Each job listing is structured as:
```json
{
  "title": "Job Title",
  "company": "Company Name",
  "about": "Job description summary",
  "location": "Job location",
  "deadline": "Application deadline",
  "url": "Full job listing URL"
}
```

## Technical Details
- **Framework**: Scrapy 2.11+
- **Browser Automation**: Playwright
- **Header Rotation**: ScrapeOps
- **Database**: PostgreSQL
- **Concurrency**: 16 concurrent requests
- **Throttling**: 1 second delay between requests

## License
This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for details.
