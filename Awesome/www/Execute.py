import orm,asyncio
from models import User, Blog, Comment
loop = asyncio.get_event_loop()
@asyncio.coroutine
def test():
    yield from orm.create_pool(loop,user='www-data', password='www-data', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()
    #关闭event loop之前首先关闭连接池
    yield from orm.destory_pool()

loop.run_until_complete(test())
loop.close() #然后从容地关闭event loop
