import boto3

s3 = boto3.client('s3')
import json

bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket='mybuckets', policy=bucket_policy)
s3.delete_bucket_policy(Bucket='mybuckets')



