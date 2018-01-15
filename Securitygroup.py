import boto3

ec2 = boto3.client('ec2')

ec2.describe_regions()

###Availability zones
response = ec2.describe_availability_zones()
print(response[AvailabilityZones])

