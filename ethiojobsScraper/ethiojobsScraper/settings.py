from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()


BOT_NAME = "ethiojobsScraper"

SPIDER_MODULES = ["ethiojobsScraper.spiders"]
NEWSPIDER_MODULE = "ethiojobsScraper.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "ethiojobsScraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Concurrency and throttling settings
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     # "ethiojobsScraper.middlewares.EthiojobsscraperSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #    "ethiojobsScraper.middlewares.EthiojobsscraperDownloaderMiddleware": 543,
    "ethiojobsScraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware": 400,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "ethiojobsScraper.pipelines.EthiojobsscraperPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
SHELL = ["ipython"]

# __________________________________________________________________________________
# SCRAPEOPS setting ===> fake user aggent
SCRAPEOPS_API_KEY = os.getenv("SCRAPEOPS_API_KEY")
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = os.getenv("SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT")

SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = os.getenv(
    "SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT"
)
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 5


# settings.py


DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,  # Set to False if you want to see the browser
}
