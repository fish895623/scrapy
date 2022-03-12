import time

from bs4 import BeautifulSoup

from crawling.items import CrawlingItem
from scrapy import Request, Spider
from scrapy.selector import Selector


class RimWorldSpider(Spider):
    name = "rimworld"
    url = "294100"

    def start_requests(self):
        yield Request(
            url="https://steamcommunity.com/app/" + self.url,
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
        CardContentNewsDate = data.select(".apphub_CardContentNewsDate")
        length = len(CardContentNewsTitle)

        for number in range(length):
            item = CrawlingItem()
            item["name"] = self.name
            item["address"] = "https://steamcommunity.com/app/" + self.url
            item["title"] = CardContentNewsTitle[number].text
            item["content"] = "".join(CardTextContent[number].getText("\n"))
            item["date"] = CardContentNewsDate[number].text

            self.logger.info(item)
            yield item
