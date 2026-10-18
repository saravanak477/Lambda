import json
import boto3

s3_client=boto3.client('s3')

dynamodb_client = boto3.resource('dynamodb')

table=dynamodb_client.Table('jsontesting')

def lambda_handler(event, context):

    bucket_name='lambda-storagetesting'

    file_name='customer.json'

    s3_response=s3_client.get_object(Bucket=bucket_name,Key=file_name)


    data_contents=json.loads(s3_response['Body'].read().decode('utf-8'))

    with table.batch_writer() as batch:
        for item in data_contents:
            batch.put_item(Item=item)

    
		
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
