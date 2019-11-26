import boto3
import logging
import os

ec2 = boto3.client('ec2')
instancesidd='i-0XXX'
instance_details = ec2.describe_instances(InstanceIds=[instancesidd])
response = instance_details['Reservations'][0]['Instances'][0]['Placement']['AvailabilityZone']
print(response)
