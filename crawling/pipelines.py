import sqlite3


class CrawlingPipeline:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("asdf.sqlite")
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.curr.execute("CREATE TABLE IF NOT EXISTS prod (title TEXT, content TEXT)")

    # store items to databases.
    def process_item(self, item, spider):
        self.putitemsintable(item)
        return item

    def putitemsintable(self, item):
        self.curr.execute(
            """
            INSERT INTO prod (title, content)
            SELECT '{0}', {1}
            WHERE NOT EXISTS (SELECT 1 FROM prod WHERE title = '{0}', content = "{1}")
            """.format(
                item["title"],
                item["content"],
            ),
        )
        self.conn.commit()
