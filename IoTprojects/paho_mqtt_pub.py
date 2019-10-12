#####################################################################
# Filename:    paho_mqtt.py
# Description: Implementing an MQTT publisher to a ubidots 
#			   device, the subscriber is a raspberry pi usig
# 		       eclipse paho library.
# Notes:       payload: is a string containing the message that
#              will be published to the topic.
#			   topic: a string variable containing the topic name.
#			   qos: quality of service, number of message resend times.
# Author:      Abdulmaguid Eissa
######################################################################

import paho.mqtt.client as mqtt

broker_url  = "iot.eclipse.org"
broker_port = 1883
#topic = "put your topic here"
#token = "put your token here"

# Testing the client
client = mqtt.Client()
client.connect(broker_url, broker_port)

# Publish to the client.
client.publish(topic="TesingTopic", payload="TestingPayload", qos=1, retain=False)
print("Done!")
