# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import sqlite3


class CrawlingPipeline:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("asdf.sqlite")
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.curr.execute("CREATE TABLE IF NOT EXISTS prod(name TEXT)")

    # store items to databases.
    def process_item(self, item, spider):
        self.putitemsintable(item)
        return item

    def putitemsintable(self, item):
        self.curr.execute(
            "INSERT OR IGNORE INTO prod VALUES (?)",
            (item["name"],),  # extracting item.
        )
        self.conn.commit()
