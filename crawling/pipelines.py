import base64

from pymongo import MongoClient

pipeline = [
    {
        "$group": {
            "_id": "$title",
            "count": {"$sum": 1},
            "content": {"$first": "$content"},
        }
    },
    {
        "$match": {
            "_id": {"$ne": "null"},
            "count": {"$gt": 1},
        }
    },
    {
        "$project": {
            "_id": 0,
            "title": "$_id",
            "content": "$content",
        }
    },
]


class CrawlingPipeline:
    def __init__(self) -> None:
        self.client = MongoClient(host="localhost")
        self.db = self.client.steam

    def process_item(self, item, spider):
        self.putitemsintable(item)
        return item

    def putitemsintable(self, item):
        self.db.steam.insert_one(self.db.steam.aggregate(pipeline=pipeline))
