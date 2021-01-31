import redis
import time,random
import readconfig


def send_times(num):
    def decorator(func):
        def wrapped(*args,**kwargs):
            func(*args,**kwargs)
            
            if r.llen('phone_list') != 0:
                phone = r.rpop('phone_list')
                result = True
                while result:
                    i = 1                
                    while i <= num:
                        if random.randint(0,1) != 0:
                            print(f'发送成功: {phone}, send_times: {i}')
                            result = False
                            break
                        i +=1
                    if i > num:
                        print('1 分钟内发送次数超过 5 次, 请等待 1 分钟')
                        time.sleep(60)
        return wrapped
    return decorator


@send_times(5)
def sendsms(telephone_number: int,content: str,key=None):
    # 使用伪随机数来模拟发送失败
    if random.randint(0,1) == 0:
        r.lpush('phone_list',telephone_number)
    else:
         print(f'发送成功: {telephone_number}')

   

redis_config = readconfig.read_config()
pool = redis.ConnectionPool(**redis_config)
r = redis.Redis(connection_pool=pool)


if __name__ == "__main__":
    sendsms(12345654321, content="hello") 
    sendsms(12345654322, content="hello") 