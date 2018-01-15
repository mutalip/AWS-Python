#Create, delete and monitor EC2 instances

import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)


#monitor
response = ec2.monitor_instances(InstanceIDs=['instanceid]')

#stop
ec2.stop_instances(instaceID=['id'])

#reboot instace
ec2.reboot.instances(InstanceIds=[''])


