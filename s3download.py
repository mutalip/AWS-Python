import boto3

s3 = boto3.client('s3')

#Download file as client_file.zp Client method
s3.download_file('mybucket', 'myfile.zip', 'client_file.zip')

import botocore
s3 = boto3.resource('s3')

try:
  s3.Bucket('mybucket').download_file('myfile.zip', 'client_file.zip')
except botocore.exceptions.ClientErrors as e:
  if e.response['Error']['Code'] == '404':
    print("The object does not exist")
  else:
    raise
