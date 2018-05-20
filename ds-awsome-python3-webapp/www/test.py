import orm
import aiohttp,asyncio
from models import User, Blog, Comment


loop = asyncio.get_event_loop()
loop.run_until_complete(orm.create_pool(loop, user='root',password='',db='awesome'))

u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
loop.run_until_complete(u.save())

# @asyncio.coroutine
# def test():
#     yield from orm.create_pool(loop,user='root', password='', db='awesome')

#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

#     yield from u.save()

# for x in test():
#     pass 