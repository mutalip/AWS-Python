#!/usr/binenv python3

#Creates new user
import boto3
import json

iam = boto3.clien('iam')
response = iam.create_user(UserName= 'newuser')
print (response)
