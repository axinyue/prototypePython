
import redis
import setting


client = redis.Redis(**setting.REDIS_CONFIG)

client.set("name","456")
b = client.get("name")
print(b)