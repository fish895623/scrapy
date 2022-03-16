from bs4 import BeautifulSoup
from crawling.items import CrawlingItem
from scrapy import Request, Spider
from scrapy.selector import Selector


class SteamSpider(Spider):
    name = "steam"

    def start_requests(self):
        urls = ["294100", "1091500"]
        return [
            Request(url="https://steamcommunity.com/app/" + url, callback=self.parse)
            for url in urls
        ]

    def parse(self, response):
        hxs = Selector(response)
        data = BeautifulSoup(
            "".join(hxs.xpath("//*[contains(@class, 'Announcement_Card')]").extract()),
            "html.parser",
        )

        CardContentNewsTitle = data.select(".apphub_CardContentNewsTitle")
        CardTextContent = data.select(".apphub_CardTextContent")
        CardContentNewsDate = data.select(".apphub_CardContentNewsDate")
        length = len(CardContentNewsTitle)

        for number in range(length):
            item = CrawlingItem()
            item["name"] = response.css(".apphub_AppName::text").extract()[0]
            item["address"] = response.url
            item["title"] = CardContentNewsTitle[number].text
            item["content"] = "".join(CardTextContent[number].getText("\n"))
            item["date"] = CardContentNewsDate[number].text

            self.logger.info(item)
            return item
