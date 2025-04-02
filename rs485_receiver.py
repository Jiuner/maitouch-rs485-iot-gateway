import serial
import json
from mqtt_publisher import publish_to_mqtt

with open("config.json") as f:
    config = json.load(f)

ser = serial.Serial(config["serial_port"], config["baudrate"], timeout=1)

while True:
    line = ser.readline().decode("utf-8").strip()
    if line:
        try:
            data = dict(item.split(":") for item in line.split(";"))
            json_data = json.dumps(data)
            print("Received:", json_data)
            publish_to_mqtt(json_data)
        except Exception as e:
            print("Parsing error:", e)
