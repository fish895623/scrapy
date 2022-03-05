import base64
from pymongo import MongoClient


class CrawlingPipeline:
    def __init__(self) -> None:
        self.client = MongoClient(host="localhost")
        self.db = self.client.steam

    def process_item(self, item, spider):
        self.putitemsintable(item)
        return item

    def putitemsintable(self, item):
        self.db.steam.insert_one(
            {
                "title": item["title"],
                "content": item["content"],
            }
        )
