'''
Created on Apr 16, 2018

@author: akash
'''

import paho.mqtt.client as mqtt
import time

connflag = False    
    
def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload)+" my payload is being printed")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

def on_subscribe(client, userdata, mid, granted_qos):
    print ("client" + client 
               +"user data" + userdata
               +"mid" + mid
               + "granted_qos" + granted_qos)


    
def on_publish(client, userdata, mid):
    print ("client" + client 
               +"user data" + userdata
               +"mid" + mid)
        
        
   
def MQTTcaller(topic, payload):
    
        
       # path = self.path
       # payload = self.payload
            
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    msg = payload
    host = 'iot.eclipse.org'
    port = 1883
    
    client.connect(host, port, keepalive=60)
    i=1
    client.loop_start()
    time.sleep(2)    
    client.publish(topic, payload, qos=0, retain=False)
    print (" mqtt call done and published succcessfully============================")
    print("Message sent : " + msg)
    client.loop_stop()	    
