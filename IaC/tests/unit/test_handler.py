
# from VisitCountFunc import app# 
# # Pytest Unit Test:
# import json
# import boto3
# import pytest
# from moto import mock_dynamodb


# # The 'mock_dynamodb2' decorator is used to mimic DynamoDB for testing
# @mock_dynamodb
# def test_lambda_handler():
#     # DynamoDB resource is initialized
#     dynamodb = boto3.resource('dynamodb')
#     # Table name is stored in a variable
#     table_name = 'DynaDBTableCloudResume'
#     # Table is created with the necessary schema and throughput specifications
#     dynamodb.create_table(
#         TableName=table_name,
#         KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
#         AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'N'}],
#         ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10}
#     )
#     # The created table is fetched
#     table = dynamodb.Table(table_name)
#     # Initial view count is stored in a variable
#     initial_count = 0
#     # A record is added to the table with the initial view count
#     table.put_item(Item={'id' : 0, 'view_count': initial_count})

#     # The Lambda function is called, and we assert that it returns the incremented view count
#     new_view_count = app.lambda_handler(None, None)
#     assert new_view_count == initial_count + 1

#     # The record is fetched from the table again
#     response = table.get_item(Key={'id': 0})
#     # The stored view count is fetched from the response
#     stored_count = response['Item']['view_count']
#     # We assert that the stored view count is the incremented view count
#     assert stored_count == initial_count + 1


import unittest
from unittest.mock import patch, MagicMock
from VisitCountFunc import app  # replace 'VisitCountFunc' with the name of your Python file

class TestLambdaHandler(unittest.TestCase):
    @patch('VisitCountFunc.app.table')
    def test_lambda_handler(self, table_mock):
        # Set up the mock object
        get_item_response_mock = {'Item': {'id': '0', 'view_count': 1}}
        table_mock.get_item.return_value = get_item_response_mock

        # Run the function
        result = app.lambda_handler({}, {})

        # Assert the results
        self.assertEqual(result, 2)
        table_mock.get_item.assert_called_once_with(Key={'id': '0'})
        table_mock.put_item.assert_called_once_with(Item={'id': '0', 'view_count': 2})

if __name__ == '__main__':
    unittest.main()
