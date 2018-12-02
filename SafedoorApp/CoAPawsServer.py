'''
Created on Apr 11, 2018

@author: akash
'''
from coapthon.server.coap import CoAP
from CoAPSafeDoorResource import*
from CoAPawsResource import*

class CoAPawsServer(CoAP):
   
    def __init__(self, ipAddr = "0.0.0.0", port = 5683, multicast = False):
        CoAP.__init__(self, (ipAddr, port), multicast)

        if port >= 1024:
            self.port = port
        else:
            self.port = 5683

        self.ipAddr = ipAddr
        self.useMulticast = multicast
        self.initAWSresources()
   
    

  

    def initAWSresources(self):
        self.add_resource('SafeDoor/',SafeDoorResource() )
        self.add_resource('AWS/', CoAPawsResource())
        
        print("CoAP server initialized. Binding: " + self.ipAddr + ":" + str(self.port))
        print(self.root.dump())
        
        
def main():
    ipAddr = "0.0.0.0"
    port = 5683
    useMulticast = False
    coapServer = None

    try:
        coapServer = CoAPawsServer(ipAddr, port, useMulticast)

        try:
            print("Created CoAP server ref: " + str(coapServer))
            coapServer.listen(10)
        except Exception:
            print("Failed to create CoAP server reference bound to host: " + ipAddr)
            pass
    except KeyboardInterrupt:
        print("CoAP server shutting down due to keyboard interrupt...")

        if coapServer:
            coapServer.close()

            print("CoAP servrer app exiting.")


if __name__ == '__main__':
    main()
        
    
