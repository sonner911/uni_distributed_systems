import redis


r = redis.Redis(host='localhost', port=6379, decode_responses=True)

sub = r.pubsub()
sub.subscribe("messages")
while True:
    msg = sub.get_message()
    if msg:
        print(msg['data'])
