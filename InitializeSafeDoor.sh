#!/bin/bash
#Variables

echo "SafeDoorDevice Initializing"

python ./SafedoorApp/CoAPawsServer.py

if [ $RESULT -eq 0 ]; then
  echo Server Started Succesfully
else
  echo Failed to start server
fi



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
