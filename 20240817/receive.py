#192.168.8.16
#501教室/LED

import paho.mqtt.client as mqtt
import redis

redis_conn = redis.Redis(host='192.168.8.16', port=6379,password='raspberry')


def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')
    redis_conn.rpush(topic,message)
    print(f"topic={topic},message:{message}")

if __name__ == '__main__':
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect('192.168.8.16')
    client.subscribe('5501教室/LED',qos=2)
    client.loop_forever()