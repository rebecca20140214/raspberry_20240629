#192.168.8.16
#client.subscribe(os.environ['REDIS_SUBSCRIBE'],qos=2)
import paho.mqtt.client as mqtt
import redis
from dotenv import load_dotenv
import os
load_dotenv()

redis_conn = redis.Redis(host=os.environ['REDIS_HOST'], port=6379,password=os.environ['REDIS_PASSWORD'])


def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')
    redis_conn.rpush(topic,message)
    print(f"topic={topic},message:{message}")

if __name__ == '__main__':
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect(os.environ['MQTT_SERVER'])
    client.subscribe(os.environ['REDIS_SUBSCRIBE'],qos=2)
    #client.subscribe("501教室/LED燈",qos=2)
    client.loop_forever()