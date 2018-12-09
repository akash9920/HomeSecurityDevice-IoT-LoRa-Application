

python ./SafedoorApp/mqtt.py

if [ $RESULT -eq 0 ]; then
  echo client is subscribed to the topic SafeDoor
else
  echo Failed to intiate the subscriber
fi