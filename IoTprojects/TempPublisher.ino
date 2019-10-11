/**
 * Implemeting a Ubidots temperature publisher application, the NodeMcu is  
 * NodeMcu also publishes some data about the humidity and the temperature.
 * Raspberry pi device is working as a subscriber to retrieve temperature 
 * event data.
 * Authtor: Abdulmaguid Eissa
 * 
*/

#include <PubSubClient.h>
#include <UbidotsESPMQTT.h>
#include <DHT.h>

#define TOKEN       "Put your token here"
#define WIFISSID    "ssid" 
#define PASSWORD    "password"
#define TOPIC       "put your topic here"
#define DHT_TYPE    (11)
#define DHT_PIN     (D6)

/*
 * Globals
**/
Ubidots client(TOKEN);
DHT dht(DHT_PIN, DHT_TYPE);
float humidity = 0.0;
float temp     = 0.0;

void callback(char* topic, byte* payload, unsigned int length) {
    Serial.print("Message arrived [");
    Serial.print(topic);
    Serial.print("] ");
    
    for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
    }
    Serial.println();
}

/****************************************
 * Main Functions
 ****************************************/

void setup() {
    Serial.begin(115200);
    client.setDebug(true); 
    client.wifiConnection(WIFISSID, PASSWORD);
    client.begin(&callback);
}

void loop() {

    if(!client.connected()){
      client.reconnect();
    }
    
    temp = dht.readTemperature();    
    client.add("temperature", temp);      // Insert your variable Labels and the value to be sent
    client.ubidotsPublish("m-to-m");      // Publish to this device
   
    client.loop();
}
