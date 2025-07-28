# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EthiojobsscraperItem(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    about = scrapy.Field()
    location = scrapy.Field()
    deadline = scrapy.Field()
    url = scrapy.Field()
