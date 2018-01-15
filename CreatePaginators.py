#Paginators are a feature of boto3 that act as an abstraction over the process of iterating over an entire result set of a truncated API operation.


import boto3

#Create client
iam = boto3.client('iam')

response = iam.create_user(UserName='newuser')

# Create a reusable Paginator
user = iam.get_paginator('list_users')

for repose user.pignate():
    print(response)
