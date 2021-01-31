from typing import Optional
from pocket import Pocket, PocketException

consumer: Optional[str] = None
access: Optional[str] = None

async def article_count():
    p = Pocket(consumer, access)
    try:
        return len(
            p.retrieve(offset=0)['list']
        )
    except PocketException as e:
        return e.message
