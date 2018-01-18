import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName = 'newtable',
    KeySchema = [
        {
          'AttributeName': 'username',
          'KeyType' : 'HASH'
          },
        {
          'AttributeName': 'lastname',
          'KeyType' : 'RANGE'
          }
     ],
          
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 's'
         },
    
        {
            'AttributeName': 'lastname',
            'AttributeType': 's'
         }
    ],
    
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
table.meta.client.get_waiter('table_exists'.wait(TableName='newtable')
print(table.item_count)

# if result == 0 than success

#date of table created
table = dynamodb.Table('newtable')
print(table.creation_date_time)

table.put_item(
    item={
    'username': 'mutalip',
    'firstname': 'mutalip',
    'lastname': 'kurban',
    'age': '35',
    'account_type': standard_user
    })
    
 #Get item from table
 
 response = table.get_item(
        key = {
                'username': 'mutalip',
                'lastname': 'kurban',
                        }
 )
 
 item = response['item']
 print(item)
 
 
 
 table.update_item(
        key={
              'username': 'mutalip',
              'lastname': 'kurban', 
            }
        UpdateExpression = 'SET age =  :value1',
        ExpressionAttributeValue={
        ':value1': 25
        }
    )
 
 
 print("after update")
  #Get item from table
 
 response = table.get_item(
        key = {
                'username': 'mutalip',
                'lastname': 'kurban',
                        }
 )
 
 item = response['item']
 print(item)
 
 
