
import boto3

ec2 = boto3.client('ec2')

#See existing key pairs
ec2.describe_key_pairs()

#create new key pairs
ec2.create_key_pair(KeyName='New_key')

#Check the newly created keypairs
ec2.describe_key_pairs()

#delete the key pair
ec2.delete_key_pair(KeyName='New_key')

#Check keypairs
ec2.describe_key_pairs()
