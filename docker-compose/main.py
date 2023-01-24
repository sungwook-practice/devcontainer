import redis

r = redis.Redis(host='redis', port=6379, db=0)
try:
  r.set('hello', 'world')
except Exception as e:
  print("[-] redis connection error. please check redis host and port")
