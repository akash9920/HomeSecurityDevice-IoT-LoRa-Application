'''
Created on Apr 7, 2018

@author: akash
'''
import json
import datetime

import paho.mqtt.client as mqtt

global awsValue

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


#def on_connect(client, userdata, flags, rc):
#    print("Connection returned result: "+connack_string(rc))




def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload)+" This is the result of the image comparison")
   
    getPayloadValue(msg.payload)	
    return msg.payload



#def on_message(client, userdata, message):
 #   print("Received message '" + str(message.payload) + "' on topic '"
  #      + message.topic + "' with QoS " + str(message.qos))

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

def getPayloadValue(data):
	
	awsValue = json.loads(data)
	print("												   ")
	print("												   ")
	print("												   ")
	print("												   ")
	print("												   ")
	print("		===========================================================================================")
	print("		================================== SafeDoor Message log ===================================")
	print("		===========================================================================================")	
	print("												   ")
	print("		--------------------------------------------------------------------------------------------")
	print("		===========  (1) Status:   		 	  " +awsValue["HomeSecurity"]['Status']+       "       ============")
	print("		===========  (2) Location:   		 	 " +awsValue["HomeSecurity"]['Where']+         "   ============")
	print("		===========  (3) Type:   		 	  " +awsValue["HomeSecurity"]['Type']+         "  ============")
	print("		===========  (4) Dare and Time of  Detection:     " +awsValue["HomeSecurity"]['LastPollTime']+ "    ============")
	print("		===========  (5) Confidence of Face Match 	  " +awsValue["HomeSecurity"]['Value']+        "                 ============")
	print("		===========  (6) Information   Source:    	  " +awsValue["HomeSecurity"]['Source'] +      "           ============")
	print("												   ")
	print("		---------------------------------------------------------------------------------------------")
	print("		============================================================================================")
	print("		================================== SafeDoor Message log ====================================")
	print("		============================================================================================")	
	if awsValue["HomeSecurity"]["Value"] > 90:
		print(" 					 ")
		print(" 					 ")
		print("				==========================================")
		print("				------------------------------------------")
		print("				================== ALERT =================")
		print("				------------------------------------------")
		print("				========You have been Authorised==========")
		print("				------------------------------------------")
		print("				=========The Door is being opened=========")
		print("				------------------------------------------")
		print("				============== Welcome home ==============")
		print("				------------------------------------------")
		print("				==========================================")
		print("				------------------------------------------")
		print("				==========================================")

	




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

client.subscribe("/SafeDoor", qos=0)

#client.disconnect()
client.loop_forever()




