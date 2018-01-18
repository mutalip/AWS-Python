#RDS DB

import boto3
rds = boto3.client('rds')

try:
  dbs = rds.describe_db_instances()
  for db in dbs['DBinstances']:
    print("%s@%s:%s %s) % (db[MaterUsername], db[Endpoint][Address], db[Endpoint]['Port'], db['DNInstancesStatus']")
 
except Exception as e:
  print(e)
  
 
print("\n\r create database instances")

response = rds.create_db_instance(
    DBName='mydb',
    DBInstanceIdentifier='NewDB',
    AllocatedStorage=5,
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    MasterUsername='admin',
    MasterUserPassword='password')
   
 print(response)
 
 
 #Delete data base
 
 response = rsd.delete_db_instance(
          DBINstanceIdentifier = 'mydb'
          SkipFinalSnapshot = True
  )
  
  print (response)
 
