import json
import boto3

s3_client=boto3.client('s3')

dynamodb_client = boto3.resource('dynamodb')

table=dynamodb_client.Table('lambdabackup')

def lambda_handler(event, context):

    bucket_name='lambda-storagetesting'

    file_name='sample_csv .csv'

    s3_response=s3_client.get_object(Bucket=bucket_name,Key=file_name)

    print(s3_response)

    data_contents=s3_response['Body'].read().decode('utf-8')  

    Employees=data_contents.split('\n')

    Employees.pop(0)

    print(Employees)

    

    for customer in Employees:
        Employees=customer.split(',')
        table.put_item(
           Item={
                'id':Employees[0], 
                'lname':Employees[1],
                'fname':Employees[2],
                'age':Employees[3]
            }
       
        )
		
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
