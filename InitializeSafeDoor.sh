#!/bin/bash
#Variables

echo "SafeDoorDevice Initializing"

python ./SafedoorApp/CoAPawsServer.py

if [ $RESULT -eq 0 ]; then
  echo Server Started Succesfully
else
  echo Failed to start server
fi



<<<<<<< HEAD
python ./SafedoorApp/mqtt.py

if [ $RESULT -eq 0 ]; then
  echo client is subscribed to the topic SafeDoor
else
  echo Failed to intiate the subscriber
fi



python SafeDoorCam.py





echo "Image capture started"



echo "Image captured"

if [ $? -eq 0 ]; then
	echo "calling aws cloud"
	python 
	echo "Stack created successfully. Stack Id below: "
	echo $createOutput

else
	echo "Error in creation of stack"
	echo $createOutput
fi;
=======


>>>>>>> 7e1b89f88323029b604eae1167815591e52d3ce2
