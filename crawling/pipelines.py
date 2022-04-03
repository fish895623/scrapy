import os
from datetime import datetime

import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()


class CrawlingPipeline:
    def __init__(self) -> None:
        self.client = MongoClient(
            host='mongodb://{0}:{1}@{2}:{3}'.format(
                os.getenv('DB_USER'),
                os.getenv('DB_PASS'),
                os.getenv('DB_HOST'),
                os.getenv('DB_PORT'),
            )
        )
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
                    'date': '{0}-{1}-{2}'.format(
                        datetime.now().year, datetime.now().month, datetime.now().day
                    ),
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
