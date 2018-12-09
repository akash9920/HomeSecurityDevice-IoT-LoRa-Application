#!/bin/bash
#Variables

echo "SafeDoorDevice Initializing"

python ./SafedoorApp/CoAPawsServer.py

if [ $RESULT -eq 0 ]; then
  echo Server Started Succesfully
else
  echo Failed to start server
fi





