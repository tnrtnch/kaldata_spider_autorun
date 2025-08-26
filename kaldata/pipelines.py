import sqlite3

class KaldataPipeline:
    def __init__(self):
        self.con = sqlite3.connect('kaldata/kaldata.db')
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS kaldata(
            title TEXT,
            pubdate TEXT,             
            author TEXT,
            body TEXT
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute("SELECT * FROM kaldata WHERE title = ?", (item['title'],))
        result = self.cur.fetchone()

        if result:
            spider.logger.warn("Item already in database: %s" % item['title'])

        else:    
            self.cur.execute("""
                INSERT INTO kaldata (title, pubdate, author, body) VALUES (?, ?, ?, ?)
            """,
            (
                item['title'],
                item['pubdate'],
                item['author'],
                item['body']
            ))

            self.con.commit()
        return item