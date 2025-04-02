import paho.mqtt.client as mqtt
import json

with open("config.json") as f:
    config = json.load(f)

client = mqtt.Client()
client.connect(config["mqtt_broker"], 1883, 60)

def publish_to_mqtt(payload):
    client.publish(config["mqtt_topic"], payload)
