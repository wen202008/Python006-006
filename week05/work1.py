"""
需求描述:
在社交类网站中，经常需要对文章、视频等元素进行计数统计功能，
热点文章和视频多为高并发请求，因此采用 redis 做为文章阅读、视频播放的计数器。
"""

import redis
import threading
import readconfig

def counter(video_id: int):
    count_number = r.incr(video_id)
    return count_number

redis_config = readconfig.read_config()
pool = redis.ConnectionPool(**redis_config)
r = redis.Redis(connection_pool=pool)

if __name__ == "__main__":
    # thread_b = threading.Thread(target=counter,args=['1001'])
    print(counter(1001)) # 返回 1
    print(counter(1001)) # 返回 2
    print(counter(1002)) # 返回 1
    print(counter(1001)) # 返回 3
    # thread_b.start()
    # print(r.get('1001').decode())
    print(counter(1002)) # 返回 2

