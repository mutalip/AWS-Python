mport boto3

#Create client
iam = boto3.client('iam')

#Update username
iam.update_user(UserName='newuser', NewUserName='newuser1')


#Delete user
iam.delete_user(Username='newuser1')

