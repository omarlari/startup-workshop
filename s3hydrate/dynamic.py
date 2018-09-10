#!/usr/bin/env python
from sys import argv
from string import Template
import boto3

var1, SERVICE_ENDPOINT, S3_BUCKET = argv

filein = open( '/dynamic/index.html' )
src = filein.read()
result = src.replace("$MY_URL", SERVICE_ENDPOINT)
fileWrite = open('/dynamic/index.html', "w")
fileWrite.write(result)

s3 = boto3.client('s3')
s3.put_object(Bucket=S3_BUCKET, Body=open('/dynamic/index.html', 'rb'), ContentType='text/html', Key='index.html')
