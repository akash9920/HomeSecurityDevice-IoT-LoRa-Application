'''
Created on Apr 11, 2018

@author: akash
'''
import socket

from CoAPawsResource import*
from CoAPSafeDoorResource import*

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri

class CoAPawsClient:
    
    def __init__(self, host, port, path):
        if host and not host.isspace():
            self.host = host
        else:
            self.host = "localhost"

        if port >= 1024:
            self.port = port
        else:
            self.port = 5683

        self.serverAddr = (self.host, self.port)

        if path and not path.isspace():
            self.path = path
        else:
            self.path = "SafeDoor"

        self.url = "coap://" + self.host + ":" + str(self.port) + "/" + self.path

        try:
            print("Parsing URL: " + self.url)
            
            
            self.host, self.port, self.path = parse_uri(self.url)

            tmpHost = socket.gethostbyname(self.host)

            if tmpHost:
                self.host = tmpHost
            else:
                print("Can't resolve host: " + self.host)
                pass

        except socket.gaierror:
            print("Failed to resolve host: " + self.host)
            
    
    
    def initClient(self):
        try:
            self.client = HelperClient(server=(self.host, self.port))

            print("Created CoAP client ref: " + str(self.client))
            print(" coap://" + self.host + ":" + str(self.port) + "/" + self.path)
        except Exception:
            print("Failed to create CoAP helper client reference using host: " + self.host)
            pass
        
    def handleGetTest(self, path):
#         path = self.path
        self.initClient()
        
        if not path and self.pathList:
            for pathEntry in self.pathList:
                print("Testing GET with path entry: " + pathEntry)
                response = self.client.get(pathEntry)
                
                print ("This is get method of ---------")
                print (response)
                
                if response:
                    print(response.pretty_print())
                    return response
                else:
                    print("No response received for GET on path entry: " + pathEntry)

        elif path:
            print("Testing GET with path: " + path)

            response = self.client.get(path)

            if response:
                print(response.pretty_print())
                return (response)
            else:
                print("No response received for GET on path: " + path)

        else:
                print("Can't test GET - no path or path list provided.")

        self.client.stop()
    
    def handlePostTest(self, path, payload):

        print("Testing POST with path: " + path + ", payload: " + payload)

        self.initClient()

        response = self.client.post(path, payload)
        
        print ("-----this is handle post test method----")
        print (response)

        if response:
            print ("This is printing of response")
            print(response.pretty_print())
            print (response)
            

        else:
            print("No response received.")

        self.client.stop()

    def handlePutTest(self, path, payload):

        print("Testing PUT with path: " + path + ", payload: " + payload)

        self.initClient()

        response = self.client.put(path, payload)

        if response:
            print(response.pretty_print())
        else:
            print("No response received.")

        self.client.stop()
        
    def handleDeleteTest(self, path):

        print("Testing DELETE with path: " + path)

        self.initClient()

        response = self.client.delete(path)

        if response:
            print(response.pretty_print())
        else:
            print("No response received.")

        self.client.stop()
        
    def runTest(self,data):
        
	#data = "Jhanvi Preashan shalalalal"
        payload = data 
        
        
        print ("=========handling post============")
        self.handlePostTest(self.path, payload)  
         
        print ("============handling get================")
        self.handleGetTest(self.path)
    
'''    
def main():
        
#     coapCLient = CoAPawsClient('californium.eclipse.org', 5683, 'SafeDoor')
    coapCLient = CoAPawsClient("localhost", 5683, "/SafeDoor")
    
#     coapCLient1 = CoAPawsClient("localhost", 5683, "AWS") 
        
      
    print("======================coapClient  run test 1-==============")  
    coapCLient.runTest("akash anandiiiiiiiiiiiiieeieiie")
#     print("======================coapClient  run test 1-==============") 
#     coapCLient1.runTest()
    
if __name__ == '__main__':
    main()
            
'''            
            

    
