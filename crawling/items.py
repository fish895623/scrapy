from scrapy import Field, Item


class CrawlingItem(Item):
    name = Field()
    address = Field()
    title = Field()
    content = Field()
    date = Field()
    pass
