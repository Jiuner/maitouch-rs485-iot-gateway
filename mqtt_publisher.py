import paho.mqtt.client as mqtt
import json
import logging

logging.basicConfig(level=logging.INFO)

with open("config.json") as f:
    config = json.load(f)

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info(f"Connected to MQTT Broker: {config['mqtt_broker']}")
    else:
        logging.error(f"Failed to connect to MQTT Broker, return code {rc}")

def on_disconnect(client, userdata, rc):
    logging.warning("MQTT disconnected, attempting to reconnect...")
    try:
        client.reconnect()
    except Exception as e:
        logging.error(f"Reconnection failed: {e}")

client.on_connect = on_connect
client.on_disconnect = on_disconnect

try:
    client.connect(config["mqtt_broker"], 1883, 60)
except Exception as e:
    logging.critical(f"Initial MQTT connection failed: {e}")

client.loop_start()

def publish_to_mqtt(payload):
    logging.info(f"Publishing to {config['mqtt_topic']}: {payload}")
    client.publish(config["mqtt_topic"], payload)
