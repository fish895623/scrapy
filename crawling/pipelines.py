from datetime import datetime

from pymongo import MongoClient


class CrawlingPipeline:
    def __init__(self) -> None:
        self.client = MongoClient(host='mongodb://root:example@localhost')
        self.db = self.client.steam

    def process_item(self, item, spider):
        self.putitemsintable(item)
        return item

    def putitemsintable(self, item):
        if self.db.steam.find_one({'title': item['title']}) is None:
            self.db.steam.insert_one(
                {
                    'name': item['name'],
                    'address': item['address'],
                    'title': item['title'],
                    'content': item['content'],
                    'date': datetime.now().strftime('%Y-%-m-%d'),
                }
            )
        else:
            self.db.steam.update_one(
                {'title': item['title']},
                {
                    '$set': {
                        'name': item['name'],
                        'address': item['address'],
                        'content': item['content'],
                    }
                },
            )
