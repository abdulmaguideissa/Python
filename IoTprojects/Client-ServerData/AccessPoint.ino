/**
 * Implemeting an Access point to establish a local M2M with  
 * the NodeMCU as server AP and the raspberry pi as client.
 * Authtor: Abdulmaguid Eissa
 * 
*/

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

/**
 * Definitions
*/
#define LED       D5
#define APSSID    ("nodeaccesspoint")
#define APPSK     ("NodeMcuAp")
#define WSPORT    (80) // web server port

#define BUILTIN_HIGH   LOW
#define BUILTIN_LOW    HIGH

/**
 * Globals
*/
ESP8266WebServer server(WSPORT);

// handel client requests
void handle_root(void) {
    
    digitalWrite(LED_BUILTIN, BUILTIN_LOW);
    
    // check on the query inputs first
    if(server.argName(0) == "led") {
        if(server.arg(0) == "on") {
            digitalWrite(LED_BUILTIN, BUILTIN_HIGH);
            Serial.println("Led is on");
        }
        else if(server.arg(0) == "off"){
            digitalWrite(LED_BUILTIN, BUILTIN_LOW);
            Serial.println("Led is off");
        }
    }

    // send server response
    server.send(200, "/text/html", "OK");
}


// Main setup function  
void setup() {
    // Led initializartions
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, BUILTIN_LOW);

    // Serial initializations
    Serial.begin(115200);
    delay(2000);

    Serial.println("Configuring access point...");

    // setup soft access point
    while(WiFi.softAP(APSSID, APPSK) == false) {
        delay(500);
        Serial.print(".");
    }
    
    Serial.println("\nAccess point was setup successfully");
    IPAddress ip = WiFi.softAPIP();
    Serial.println("\nAccess point IP address is: ");
    Serial.println(ip);

    // up the server with the user task
    server.on("/", handle_root);
    server.begin();
    Serial.println("Http server started");
}

// Main loop
void loop() {
    server.handleClient();
}
