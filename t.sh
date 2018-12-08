#!/bin/bash

getDate=$(date "+%d-%b-%Y@%H:%M:%S")  


cp image.jpg "image_$getDate.jpg" 

aws s3 cp "image_$getDate.jpg" s3://safedooruserhistory




