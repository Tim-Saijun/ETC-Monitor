import redis
import json

# r = redis.Redis(host='node4', port=6379, db=0, password='redis_password',\
#                 decode_responses=True, charset='UTF-8', encoding='UTF-8')
# r.hset("my-hash-key","1","23")
def get_alarm_fromRedis():
    r = redis.Redis(host='node4', port=6379, db=0, password='redis_password', decode_responses=True, charset='UTF-8', encoding='UTF-8')
    alarm = r.hgetall("my-hash-key")
    if len(alarm) > 0:
        # alarm = json.loads(alarm)
        print(alarm)
        return alarm
    else:
        return None
alarm = get_alarm_fromRedis()
#将alarm转换为json格式,中文显示正常
alarm = json.dumps(alarm, ensure_ascii=False)
#将alarm转换为http响应格式
alarm = "HTTP/1.1 200 OK\rContent-Type: application/json\r" + alarm
print(alarm)

print(alarm)
# r.expire("my-hash-key", 6)
# print(r.hgetall("my-hash-key"))
# print(r.hmget("my-hash-key", "松山湖南"))
"""
# 获取redis数据库连接
r = redis.StrictRedis(host="node4", port=6379, db=0)
# redis存入键值对
r.set(name="key", value="value")
# 读取键值对
print(r.get("key"))
# 删除
print(r.delete("key"))

# redis存入Hash值
r.hset(name="name", key="key1", value="value1")
r.hset(name="name", key="key2", value="value2")
# 获取所有哈希表中的字段
print(r.hgetall("name"))
# 获取所有给定字段的值
print(r.hmget("name", "key1", "key2"))
# 获取存储在哈希表中指定字段的值。
print(r.hmget("name", "key1"))
# 删除一个或多个哈希表字段
print(r.hdel("name", "key1"))
# 过期时间
r.expire("name", 60)  # 60秒后过期
# 更多相关内容可以参考菜鸟教程
"""
