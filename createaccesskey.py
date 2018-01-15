mport boto3

#Create client

iam = boto3.client('iam')
response = iam.create_access_key(UserName='newuser')
print(response[AccessKey])


