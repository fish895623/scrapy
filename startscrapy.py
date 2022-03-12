from crawling import settings
from crawling.spiders.rimworld import RimWorldSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(RimWorldSpider)
    process.start()
