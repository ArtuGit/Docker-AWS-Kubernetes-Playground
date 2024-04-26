from dotenv import dotenv_values
import redis

config = dotenv_values(".env")

redis_host = config['REDIS_HOST']
redis_port = config['REDIS_PORT']

print(f"Establishing Redis connection host: {redis_host}, port: {redis_port}")
r = redis.Redis(host=config['REDIS_HOST'], port=config['REDIS_PORT'])

print('Python script is run.')
