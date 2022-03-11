import scrapy


class CrawlingItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    pass
