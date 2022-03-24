import sys

from crawling import settings
from crawling.spiders.steam import SteamSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

if __name__ == '__main__':
    for i in sys.argv:
        print(i)
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(SteamSpider)
    process.start()
