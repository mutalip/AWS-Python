import boto3
s3 = boto3.client('s3')

#Create core configuration
cors_configuration = { 
  'CORSRules': [{
        'AllowedHeaders': ['Authorization'],
        'AllowedMethods': ['GET', 'PUT'],
        'AllowedOrigins': ['*'],
        'ExposeHeaders': ['GET', 'PUT'],
        'MaxAgeSeconds': 3000
  
  }]
}



result = s3.get_bicket_cors(Bucket='mybucket')
s3.put_bucket_cors(Bucket='my-bucket', CORSConfiguration=cors_configuration)
