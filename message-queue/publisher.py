import redis


r = redis.Redis(host='localhost', port=6379, decode_responses=True)

while True:
    message = input()
    r.publish("messages", message)
