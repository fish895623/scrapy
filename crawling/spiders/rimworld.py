from operator import length_hint
from scrapy import Spider, Request
import re

from crawling.items import CrawlingItem
from scrapy.selector import Selector
from bs4 import BeautifulSoup


class RimWorldSpider(Spider):
    name = "rimworld"

    def start_requests(self):
        yield Request(
            url="https://steamcommunity.com/app/294100",
            callback=self.parse_title,
        )

    def parse_title(self, response):
        hxs = Selector(response)
        data = BeautifulSoup(
            "".join(hxs.xpath("//*[contains(@class, 'Announcement_Card')]").extract()),
            "html.parser",
        )
        CardContentNewsTitle = data.select(".apphub_CardContentNewsTitle")
        CardTextContent = data.select(".apphub_CardTextContent")
        length = len(CardContentNewsTitle)

        for _ in range(length):
            item = CrawlingItem()
            for ContentNewsTitle in (i for i in CardContentNewsTitle):
                item["title"] = ContentNewsTitle.text
            for TextContent in (i for i in CardTextContent):
                item["content"] = "".join(TextContent.getText("\n"))
                yield item
