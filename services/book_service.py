import datetime
from goodreads import client
from typing import Optional

API_DOCS = 'https://www.goodreads.com/api'
USER_ID = '28892852'
key: Optional[str] = None
secret: Optional[str] = None

now = datetime.datetime.now()

class Client():

    def __init__(self):
        self.gc = client.GoodreadsClient(
            key, secret)

    async def books_on_shelf_count(self, shelf_label=f'read-{now.year}'):
        res = self.gc.request('shelf/list.xml',{'page':'1', 'user_id':USER_ID})
        for shelf in res['shelves']['user_shelf']:
            if shelf['name'] == shelf_label:
                return int(shelf['book_count']['#text'])

        return self.no_shelf_code

    @property
    def no_shelf_code(self):
        return '[no shelf]'
