import scrapy


class EthiojobsSpider(scrapy.Spider):
    name = "ethiojobs"
    allowed_domains = ["ethiojobs.net"]

    def start_requests(self):
        url = "https://ethiojobs.net/jobs"
        yield scrapy.Request(url, meta={"playwright": True})

    def parse(self, response):
        job_cards = response.css("div.job-card-item-container")
        print(f"Found {len(job_cards)} job listings")

        for job in job_cards:

            main = job.css(
                "div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-9.mui-style-rrl33y"
            )

            yield {
                "title": main.css("a ::text").get(),
                "company": job.xpath(
                    ".//div[contains(@class,'MuiGrid-container')][.//p[contains(text(),'by')]]//a/button/text()"
                ).get(),
                "about": job.css(
                    "p.MuiTypography-root.MuiTypography-body1.mui-style-10rtjdg::text"
                ).get(),
                "location": job.xpath(
                    ".//img[@alt='location']/following-sibling::p/text()"
                ).get(),
                "Deadline": job.xpath(
                    ".//img[@alt='employment']/following-sibling::p/text()"
                ).get(),
                "url": response.urljoin(main.css("a::attr(href)").get()),
            }

        pagination_list = response.xpath(
            '//button[starts-with(@aria-label, "Go to page") or starts-with(@aria-label, "page ")]'
        )
        last_page = pagination_list[-1].xpath("./@aria-label").get().strip().split()[-1]

        for page in range(1, int(last_page) + 1):
            next_page_url = f"https://ethiojobs.net/jobs?page={page}&isFeatured=false"
            print("next_page_url:", next_page_url)
            yield scrapy.Request(
                next_page_url, callback=self.parse, meta={"playwright": True}
            )
