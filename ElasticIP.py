import boto3

ec2 = boto3.client('ec2')
print(ec2)

filter = [{'Name': 'domain', 'Values': ['vpc']}]
response = ec2.describe_addresses(Filters=filters)
print(response)


allocation = ec2.allocate_address(DOmain = 'vpc')
response = ec2.associate_address(AllocationId=allocation[''], InstanceId='i-07d92a5bd6b30f35c')
