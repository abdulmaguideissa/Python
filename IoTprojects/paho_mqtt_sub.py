#####################################################################
# Filename:    paho_mqtt.py
# Description: Implementing an MQTT subscriber to a ubidots 
#			   device, the subscriber is a raspberry pi usig
# 		       eclipse paho library.
# Notes:       payload: is a string containing the message that
#              will be published to the topic.
#			   topic: a string variable containing the topic name.
#			   qos: quality of service, number of message resend times.
# Author:      Abdulmaguid Eissa
######################################################################

import time
import paho.mqtt.client as mqtt
import sys
import os
import RPi.GPIO as GPIO

######################
# raspberrypi setup

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

#######################
# server globals

connected   = False
broker_url  = "industrial.api.ubidots.com"
broker_port = 1883
Token    = "BBFF-3sxGXzs765VxZ7tdMSKZtcOpQkBr3E"
Device   = "m-to-m"
Variable = "trigger"
topic    = "/v1.6/devices/"
Topic    = "{}/{}".format(Device, Variable)
url      = "{}/api/v1.6.devices/{}/{}/lv".format(broker_url, Device, Variable)
password = ""
temp_sts = ""

# Payload function, callbacks, to print a message to the subscriber.
def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("[INFO] connected to {}".format(broker_url))
	else:
		print("[INFO] Failed to connect, result code: {}".format(rc))

def on_subscribe(client, userdata, mid):
	print("Subscribed to {} successfully".format(Variable))

def on_disconnect(client, userdata, rc):
	print("Client got disconnected")

def on_message(client, userdata, message):
	temp_sts = message.payload
	print("Message received: " + str(message.payload))

def on_log(client, obj, level, string):
	print(string)

# Main function 
def main():
	try:
		mqtt_client = mqtt.Client(None, True, None)
		mqtt_client.username_pw_set(Token, password)
		mqtt_client.on_message = on_message
		mqtt_client.on_connect = on_connect
		mqtt_client.on_subscribe = on_subscribe
		#mqtt_client.on_log = on_log
		mqtt_client.connect(broker_url, broker_port)
		mqtt_client.loop_start()
		res = mqtt_client.subscribe(Topic, 0)
		
		if str(temp_sts) == "0.0":
			GPIO.output(11, True)
			print("Winter has come :)")
		elif str(temp_sts) == "1.0":
			GPIO.output(11, False)
			print("We still in the south :(")
	except Exception as e:
		print("[ERROR] {}".format(e))
	

if __name__ == '__main__':
	while True:
		main()
		time.sleep(60)



