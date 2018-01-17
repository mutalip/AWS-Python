import boto3
import botocore

cors_configuration = {
  'CORSRules' : [{
    ''Allow
  
  }]
}

s3 = boto3.client('s3')

result = s3.get_bicket_cors(Bucket='mybucket')
