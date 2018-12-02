
import json
import datetime

d = {'Topic' :'Security'}
#print (json.dumps(d))

v1 = None
v2 = None
v3 = None

def setv1(x):
    global v1
    v1 = x
    
def setv2(x):
    global v2
    v2 = x

def setv3(x):
    global v3
    v3 = x
    
    
setv1(" new String")
setv2(5)
setv3("another new string")




d["Topic"] = dict()
d["Topic2"] = dict()

d["Topic"]['Status'] = v1
d["Topic"]['Type'] = 'Secure'
d["Topic"]['LastPollTime'] = str(datetime.datetime.now())
d["Topic"]['Value'] = v2
d["Topic"]['Source'] = v3
     
#def myconverter(o):
 #   if isinstance(o, datetime.datetime):
  #      return str(o)
    
#json.dumps(d)    


ak = json.dumps(d)

print(ak)
print(d)

an = json.loads(ak)

print (an)

for key in an:
    for k in an[key]:
        print k
        print an[key][k]

print (an["Topic"]["Value"]) 


