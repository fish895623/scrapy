from datetime import datetime

from pymongo import MongoClient


class CrawlingPipeline:
    def __init__(self) -> None:
        self.client = MongoClient(host='mongodb://root:example@192.168.0.6')
        self.db = self.client.steam

    def process_item(self, item, spider):
        self.put_items_in_table(item)
        return item

    def put_items_in_table(self, item):
        if self.db.steam.find_one({'title': item['title']}) is None:
            self.db.steam.insert_one(
                {
                    'name': item['name'],
                    'address': item['address'],
                    'title': item['title'],
                    'content': item['content'],
                    'date': f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}',
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
