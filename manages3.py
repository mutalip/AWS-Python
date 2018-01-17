import boto3

s3 = boto3.client('s3')
response == s3.list_buckets()

print (response)

#Manage buckets
buckets = [bucket['Name'] for bucket in response['Buckets']]
print ("Buckets Name %s", %buckets)

#create bucket

s3.create_bucket(Bucket = 'mybucket1', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

#file upload
filename = 'myfile.zip'
bucketname = 'mybucket'
s3.upload_file(filename, bucketname, filename)

