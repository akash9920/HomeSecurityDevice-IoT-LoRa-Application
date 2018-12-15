#!/bin/bash


python SafeDoorCam.py

aws s3 cp "image.jpg" s3://safedoor

getDate=$(date "+%d-%b-%Y@%H:%M:%S")

cp image.jpg "image_$getDate.jpg" 

aws s3 cp "image_$getDate.jpg" s3://safedooruserhistory


if [ $? -eq 0 ]; then
  echo Image captured and being pushed to the cloud
else
  echo Failed to capture the image, Please check the device
fi


python ./SafedoorApp/AWSRekognition.py

if [ $? -eq 0 ]; then
  echo Image Analysis Done
else
  echo Failed to perform Image Analysis on AWS server
fi


python SafeDooremail.py

if [ $? -eq 0 ]; then
  echo Notifying the authorized user
else
  echo Failed to notify the user
fi

rm image.jpg
rm "image_$getDate.jpg"
aws s3 rm s3://safedoor/image.jpg



