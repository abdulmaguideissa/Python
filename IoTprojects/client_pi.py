############################################################
# Filename:    client_pi.py
# Description: Operating the raspberry pi to work as client 
#			   to a NodeMCU server in a local M2M network.
# Author:      Abdulmaguid Eissa
#############################################################

import RPi.GPIO as GPIO
import time
import requests

switch = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch, GPIO.IN)

accesspoint = "nodeaccesspoint"
password    = "NodeMcuAp"
host        = "192.168.1.6"
url         = "http://{}".format(host)
on_led      = "{}/?led=on".format(url)
off_led     = "{}/?led=off".format(url)

# using http GET request to send the led on, led off query
# to the server node.

def main():
	try:
		if GPIO.input(switch) == True:
			# send led on query through http
			print("Switch was pressed")
			get_request = requests.get(on_led)
			http_response = get_request.status_code
			print(http_response)
		elif GPIO.input(switch) == False:
			# send led off query through http
		  	print("Switch is released")
			get_request = requests.get(off_led)
			http_response = get_request.status_code
			print(http_response)
	except Exception as e:
		print("[ERROR]: {}".format(e))

if __name__ == "__main__":
	while True:
		main()
		time.sleep(1)

