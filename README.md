# maitouch-rs485-iot-gateway

A lightweight Python-based RS-485 to MQTT gateway for integrating AI sensing data (e.g., from m’AI Touch) into IoT platforms.

## Features
- Reads RS-485 serial data via USB interface
- Parses sensor data into structured JSON
- Publishes real-time messages to MQTT broker
- Easily integrates with platforms like Node-RED, ThingsBoard, Home Assistant

## Requirements
- Python 3.x
- USB-to-RS485 converter
- MQTT broker (local or cloud)

## Setup
1. Clone this repo and install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Configure `config.json` with your serial port and MQTT settings.

3. Run the receiver:
   ```
   python rs485_receiver.py
   ```

## Example RS-485 Data Format
```
ID:01;X:123;Y:456;Z:78
```

## License
MIT
