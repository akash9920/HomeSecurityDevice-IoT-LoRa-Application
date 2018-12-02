'''
Created on Apr 7, 2018

@author: akash
'''
import boto3
import urllib

#mqtt Imports

import paho.mqtt.client as mqtt
from CoAPawsClient import*

#raspberry pie import

from time import sleep
#from boto3.dynamodb.types import NULL
#from pyasn1.compat.octets import null

import json
import datetime





#creating the payloads


def CreatAWSPayload(status,location,Type,Value,Source):


	awsJsonPayload = {}
	awsJsonPayload["HomeSecurity"] = dict()

	awsJsonPayload["HomeSecurity"]['Status'] = status
	awsJsonPayload["HomeSecurity"]['Where'] = location
	awsJsonPayload["HomeSecurity"]['Type'] = Type
	awsJsonPayload["HomeSecurity"]['LastPollTime'] = str(datetime.datetime.now())
	awsJsonPayload["HomeSecurity"]['Value'] = Value
	awsJsonPayload["HomeSecurity"]['Source'] = Source

	ak = json.dumps(awsJsonPayload)
	return ak



def on_connect(client, userdata, flags, rc):
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


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)



#for i in range(1,3):
#    Call_AWS(i)



def Call_AWS():

    if __name__ == "__main__":

        bucket='safedoor'
        sourceFile= 'authUser.jpg'

        targetFile='image.jpg'


    client=boto3.client('rekognition','us-east-1')

    response=client.compare_faces(SimilarityThreshold=70,
                          SourceImage={'S3Object':{'Bucket':bucket,'Name':sourceFile}},
                          TargetImage={'S3Object':{'Bucket':bucket,'Name':targetFile}})



    if response['FaceMatches'] != []:
        
        for faceMatch in response['FaceMatches']:
            position = faceMatch['Face']['BoundingBox']
            confidence = str(faceMatch['Face']['Confidence'])
            print('The face at ' + str(position['Left']) + ' ' + str(position['Top']) +       ' matches with ' + confidence + '% confidence')

           # print (confidence)

            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message

            client.connect("iot.eclipse.org", 1883, 60)
            
            a = str(confidence)
            client.publish("SafeDoor", payload = "The face has been matched with confidence value"+ a, qos=0, retain=False)
            return a
    else:
        
    
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect("iot.eclipse.org", 1883, 60)    
        #a = str(confidence)
       
        
        client.publish("SafeDoor", payload = "No match found", qos=0, retain=False)
        
        return 0




def callingAPI():
        Call_AWS()
        awsPayload = Call_AWS()
	print(awsPayload)       
        if awsPayload != 0:
		print ("A match is found")
	        coapCLient = CoAPawsClient("localhost", 5683, "SafeDoor")
		
		newJsonAWSpayload = CreatAWSPayload("Person Detected on Door"," Saint Alphonsus St. Boston ","SafeDoor AWS Security System",awsPayload,"SafeDoorApplication")
		

    	        coapCLient.runTest(newJsonAWSpayload)
                break
        else:
		print("NO Match Found")
               # coapCLient = CoAPawsClient("localhost", 5683, "SafeDoor")
                
               # newJsonAWSpayload = CreatAWSPayload("Person Standing","Akash's Laptop","Safe AWS Security",50,"SafeDoorApplication")
                #coapCLient.runTest(newJsonAWSpayload)

            
            
           

# ak = False
# while True:
#     if ak == True:
#         callingAPI()
        
#         ak = False
    
#     elif ak == False:
#         print "Sensor is off"
#         sleep(10)
#         ak =True
        
   

def main():
    callingAPI()

    
        
if __name__ == '__main__':
    
    main()
    
