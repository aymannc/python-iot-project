import json
import random
import threading
from datetime import datetime

import paho.mqtt.client as mqtt


def on_connect(client, userdata, rc):
    if rc != 0:
        pass
        print("Unable to connect to MQTT Broker...")
    else:
        print("Connected with MQTT Broker: " + str(MQTT_Broker))


def on_publish(client, userdata, mid):
    pass


def on_disconnect(client, userdata, rc):
    if rc != 0:
        pass


def publish_To_Topic(topic, message):
    mqttc.publish(topic, message)
    print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
    print("")


# Code used as simulated Sensor to publish some random values to MQTT Broker
def get_humidity_level(humidity_level):
    if humidity_level <= 30:
        return 'LOW'
    elif humidity_level <= 60:
        return 'MEDUIM'
    else:
        return 'HIGH'


def get_temperature_level(temperature_value):
    if temperature_value <= 5:
        return 'VERY COLD'
    elif temperature_value <= 15:
        return 'COLD'
    elif temperature_value <= 25:
        return 'NORMAL'
    elif temperature_value <= 35:
        return 'HOT'
    else:
        return 'VERY HOT'


def getRandomNumber():
    m = float(10)
    s_rm = 1 - (1 / m) ** 2
    return (1 - random.uniform(0, s_rm)) ** .5


def publish_Temperature_Sensor_Values_to_MQTT():
    threading.Timer(2.0, publish_Temperature_Sensor_Values_to_MQTT).start()
    global toggle
    if toggle == 0:
        temperature_value = float("{0:.2f}".format(random.uniform(10, 100) * getRandomNumber()))
        temperature_data = {'Sensor_ID': "Temperature-Sensor1",
                            'Date': (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"),
                            'Temperature': temperature_value,
                            'TemperatureLevel': get_temperature_level(temperature_value)}
        temperature_json_data = json.dumps(temperature_data)
        print("Publishing Temperature Value: " + str(temperature_value) + "...")
        publish_To_Topic(MQTT_Topic_Temperature, temperature_json_data)
        toggle = 1
    else:
        # ... iden to Temperature bloc
        toggle = 0


def publish_Humidity_Sensor_Values_to_MQTT():
    threading.Timer(2.0, publish_Humidity_Sensor_Values_to_MQTT).start()
    global toggle
    if toggle == 0:
        humidity_value = float("{0:.2f}".format(random.uniform(10, 100) * getRandomNumber()))
        humidity_data_Data = {'Sensor_ID': "Humidity-Sensor1",
                              'Date': (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f"),
                              'Humidity': humidity_value, 'HumidityLevel': get_humidity_level(humidity_value)}
        humidity_json_data = json.dumps(humidity_data_Data)
        print("Publishing Humidity Value: " + str(humidity_value) + "...")
        publish_To_Topic(MQTT_Topic_Humidity, humidity_json_data)
        toggle = 1
    else:
        # ... iden to humidity bloc
        toggle = 0


MQTT_Broker = "mqtt.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 30
MQTT_Topic_Temperature = "Home/BedRoom/DHT1/Temperature"
MQTT_Topic_Humidity = "Home/BedRoom/DHT1/Humidity"
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
toggle = 0
publish_Humidity_Sensor_Values_to_MQTT()
publish_Temperature_Sensor_Values_to_MQTT()
