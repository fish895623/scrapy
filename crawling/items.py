from scrapy import Item, Field


class CrawlingItem(Item):
    name = Field()
    address = Field()
    title = Field()
    content = Field()
    date = Field()
    pass
