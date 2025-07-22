import scrapy


class EthiojobsSpider(scrapy.Spider):
    name = "ethiojobs"
    allowed_domains = ["ethiojobs.net"]
    start_urls = ["https://ethiojobs.net/jobs"]

    def parse(self, response):
        # More flexible XPath selector using "contains"
        job_cards = response.xpath("//div[contains(@class, 'job-card-item-container')]")

        self.logger.info(f"Found {len(job_cards)} job listings")

        for job in job_cards:
            yield {
                "title": job.xpath(".//h6/text()").get(),
                "company": job.xpath(
                    ".//p[contains(@class, 'MuiTypography-root')]/text()"
                ).get(),
                "location": job.xpath(
                    ".//div[contains(text(), 'Location')]/following-sibling::div/text()"
                ).get(),
                "posted": job.xpath(
                    ".//div[contains(text(), 'Posted')]/following-sibling::div/text()"
                ).get(),
                "raw_html": job.get(),
            }
