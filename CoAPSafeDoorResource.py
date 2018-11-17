'''
Created on Apr 11, 2018

@author: akash
'''

from coapthon.resources.resource import Resource

from CoAPawsClient import*


#mqtt

import paho.mqtt.client as mqtt

from MqttCall import*


class SafeDoorResource(Resource):
    
    def __init__(self, name="SafeDoorResource", coap_server=None):

        super(SafeDoorResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)

        self.payload = ""
        self.resource_type = ""
        self.content_type = "text/plain"
        self.interface_type = ""
        

    
    
    
    
    def render_GET(self, request):
        print("Successfully retrieved this message from TestCoapResource. Payload: " + str(self.payload))
        return self
    def render_PUT(self, request):
        print("Editing stored payload: " + str(request.payload))
        self.edit_resource(request)
        print(request)
        print (self.path)
        return self
    def render_POST(self, request):
        print("Adding payload: " + str(request.payload))
        res = self.init_resource(request, SafeDoorResource())
        print (self.path) # topic
        print (request)
        print(request.payload) #MQTT PAyload
        print("MQTTcaller hass been called===============================================")
        MQTTcaller(self.path, request.payload)
        return res
    
        
        
        
    
    def render_DELETE(self, request):
        print("Delete request successful.")
        return True
    
    

            
