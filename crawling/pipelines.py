from pymongo import MongoClient


class CrawlingPipeline:
    def __init__(self) -> None:
        self.client = MongoClient(host="mongodb://root:example@localhost")
        self.db = self.client.steam

    def process_item(self, item, spider):
        self.putitemsintable(item)
        return item

    def putitemsintable(self, item):
        if self.db.steam.find({"title": item["title"]}) == None:
            self.db.steam.insert_one(
                {"title": item["title"], "content": item["content"]}
            )
        else:
            self.db.steam.update_one(
                {"title": item["title"], "content": item["content"]}
            )
