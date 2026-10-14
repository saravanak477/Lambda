import json
import boto3

#initialize the s3 client using boto3 to read data from s3 locations

s3_client = boto3.client('s3')   

def lambda_handler(event, context):
    bucket_name ='batch9-test'

#getting my s3 response to read objects

    s3_response =s3_client.list_objects_v2(Bucket=bucket_name)

#listing objetbjects in the s3 bucket

    if 'Contents' in s3_response:
        for obj in s3_response['Contents']:
            print(obj['Key'])
    else:
        print("no file in the objects")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
