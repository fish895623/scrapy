from scrapy import Spider, Request

from crawling.items import CrawlingItem


class RimWorldSpider(Spider):
    name = "rimworld"
    # custom_settings = {
    #         ""
    # }

    def start_requests(self):
        yield Request(
            url="https://steamcommunity.com/app/294100",
            callback=self.parse_title,
        )

    def parse_title(self, response):
        for sel in response.css(".apphub_CardContentNewsTitle::text"):
            item = CrawlingItem()
            item["name"] = sel.get()
            yield item
