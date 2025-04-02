# maitouch-rs485-iot-gateway

A robust RS-485 to MQTT gateway for integrating m’AI Touch sensor data into IoT systems using Python.

## Features
- Serial data acquisition via RS-485 (USB converter)
- Realtime data parsing and JSON conversion
- Secure and efficient MQTT publishing
- Logging, error handling, and MQTT reconnect logic
- Compatible with Node-RED, ThingsBoard, Home Assistant

## Installation
```bash
pip install -r requirements.txt
```

## Usage
1. Configure `config.json` with serial port and MQTT broker settings.
2. Run the gateway:
```bash
python rs485_receiver.py
```

## Example Data Format
```
ID:01;X:123;Y:456;Z:78
```

## License
MIT
