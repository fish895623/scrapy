import time

from bs4 import BeautifulSoup
from crawling.items import CrawlingItem
from scrapy import Request, Spider
from scrapy.selector import Selector


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
        time.sleep(1)
        CardContentNewsTitle = data.select(".apphub_CardContentNewsTitle")
        CardTextContent = data.select(".apphub_CardTextContent")
        length = len(CardContentNewsTitle)

        for number in range(length):
            item = CrawlingItem()
            item["title"] = CardContentNewsTitle[number].text
            item["content"] = "".join(CardTextContent[number].getText("\n"))

            self.logger.info(item)
            yield item
