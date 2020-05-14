#RDS Cloudwatch metrics boto3 get_metric_statistics()

#I have reproduced the command with the information you provided in the case.
#1. I created a IAM role with the IAM policy that you provided in the case reply.
#2. I created a new EC2 instance with the IAM role that created in step 1.
#3. I had a small python boto3 script to run get_metric_statistics() command.

#RDS Cloudwatch metrics boto3 get_metric_statistics()

==========================
[ec2-user@ip-172-31-32-121 ~]$ cat getmetricstatisticsVolumeBytesUsed.py
import boto3
cw = boto3.client('cloudwatch')
response = cw.get_metric_statistics(
        Period=3600,
        StartTime='2020-05-11T10:00:00Z',
        EndTime='2020-05-11T11:00:00Z',
        MetricName='VolumeBytesUsed',
        Namespace='AWS/RDS',
        Statistics=['Average'],
        Dimensions=[{'Name':'DBClusterIdentifier', 'Value':'myauroramysqlcluster'}]
        )
        
print (response)
[ec2-user@ip-172-31-32-121 ~]$ 
[ec2-user@ip-172-31-32-121 ~]$ python getmetricstatisticsVolumeBytesUsed.py
{u'Datapoints': [{u'Timestamp': datetime.datetime(2020, 5, 11, 10, 0, tzinfo=tzlocal()), u'Average': 1224506376192.0, u'Unit': 'Bytes'}], 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': 'ea273ddf-8d64-499b-9b8a-040534aa7c38', 'HTTPHeaders': {'x-amzn-requestid': 'ea273ddf-8d64-499b-9b8a-040534aa7c38', 'date': 'Wed, 13 May 2020 21:46:22 GMT', 'content-length': '510', 'content-type': 'text/xml'}}, u'Label': 'VolumeBytesUsed'}
[ec2-user@ip-172-31-32-121 ~]$ 
[ec2-user@ip-172-31-32-121 ~]$ aws cloudwatch get-metric-statistics --metric-name VolumeBytesUsed \
>  --start-time 2020-05-11T10:00:00Z --end-time 2020-05-11T11:00:00Z \
>  --period 3600 --namespace AWS/RDS --statistics Average \
>  --dimension="Name=DBClusterIdentifier,Value=myauroramysqlcluster"
{
    "Datapoints": [
        {
            "Timestamp": "2020-05-11T10:00:00Z", 
            "Average": 1224506376192.0, 
            "Unit": "Bytes"
        }
    ], 
    "Label": "VolumeBytesUsed"
}
==========================
