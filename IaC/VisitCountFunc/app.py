
import json
import boto3

# Set up boto3 DynamoDB resource and specify the DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DynaDBTableCloudResume')

# Use DynamoDB get_item method to retrieve the item (record) from DynamoDB that has the id '0'
def lambda_handler(event, context):
    response = table.get_item(Key={
        'id': '0'
    })

    # Check if 'Item' key exists in response
    # If so, get the 'view_count' key from 'Item' (default to 0 if 'view_count' doesn't exist)
    # If 'Item' key doesn't exist in response, this means the item doesn't exist in DynamoDB, so set view_count to 0
    if 'Item' in response:
        view_count = int(response['Item'].get('view_count', 0))
    else:
        view_count = 0  

    # Increment the view_count
    view_count += 1
    print(view_count)

    # Use DynamoDB put_item method to store the updated view_count into DynamoDB with id '0'
    response = table.put_item(Item={
        'id' : '0',
        'view_count': view_count
    })

     # Return a HTTP response with status code 200 (OK) and the updated view_count in the body
    return {
        "statusCode": 200,
        "headers": { 
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "*",
        },
        "body": json.dumps({
            'view_count': view_count 
        })
    }