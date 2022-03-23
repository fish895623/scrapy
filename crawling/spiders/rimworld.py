from bs4 import BeautifulSoup
from crawling.items import CrawlingItem
from scrapy import Request, Spider
from scrapy.selector import Selector


class SteamSpider(Spider):
    name = 'steam'

    def start_requests(self):
        urls = ['294100', '1091500']
        return [
            Request(
                url='https://steamcommunity.com/app/' + url,
                callback=self.parse,
            )
            for url in urls
        ]

    def parse(self, response, **kwargs):
        hxs = Selector(response)
        data = BeautifulSoup(
            ''.join(hxs.xpath("//*[contains(@class, 'Announcement_Card')]").extract()),
            'html.parser',
        )

        card_content_news_title = data.select('.apphub_CardContentNewsTitle')
        card_text_content = data.select('.apphub_CardTextContent')
        card_content_news_date = data.select('.apphub_CardContentNewsDate')
        length = len(card_content_news_title)

        for number in range(length):
            item = CrawlingItem()
            item['name'] = response.css('.apphub_AppName::text').extract()[0]
            item['address'] = response.url
            item['title'] = card_content_news_title[number].text
            item['content'] = ''.join(card_text_content[number].getText('\n'))
            item['date'] = card_content_news_date[number].text

            self.logger.info(item)
            return item
