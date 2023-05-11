import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DynaDBTableCloudResume')
def lambda_handler(event, context):
    response = table.get_item(Key={
        'id': '0'
    })
    view_count = response['Item']['view_count']
    view_count = view_count + 1
    print(view_count)
    response = table.put_item(Item={
        'id' : '0',
        'view_count':view_count
    })
    
    return view_count