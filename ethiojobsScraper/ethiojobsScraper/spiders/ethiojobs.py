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
            yield {
                "title": job.xpath(
                    ".//a[p[contains(@class,'MuiTypography-body1')]][last()]/p/text()"
                ).get(),
                "company": job.xpath(
                    ".//div[contains(@class,'MuiGrid-container')][.//p[contains(text(),'by')]]//a/button/text()"
                ).get(),
                "location": job.xpath(
                    ".//img[@alt='location']/following-sibling::p/text()"
                ).get(),
                "posted": job.xpath(
                    ".//img[@alt='employment']/following-sibling::p/text()"
                ).get(),
            }
            """
              <button class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary mui-style-11hluru" tabindex="0" type="button" style="background-color: inherit;"><p class="MuiTypography-root MuiTypography-body1 mui-style-okbma4" style="font-size: 13px; color: rgb(0, 0, 0); text-transform: none;">Next</p><span class="MuiTouchRipple-root mui-style-w0pj6f"></span></button>

            """
            #  https://ethiojobs.net/jobs?page=2&isFeatured=false
        pagination_list = response.xpath('//button[starts-with(@aria-label, "Go to page") or starts-with(@aria-label, "page ")]')
        last_page = pagination_list[-1].xpath("./@aria-label").get().strip().split()[-1]
 
 
 
        for page in range(1,int(last_page) + 1):
            next_page_url = f"https://ethiojobs.net/jobs?page={page}&isFeatured=false"
            print("next_page_url:", next_page_url)
            yield scrapy.Request(
                next_page_url, callback=self.parse, meta={"playwright": True}
            )
        print("Finished scraping all pages.")