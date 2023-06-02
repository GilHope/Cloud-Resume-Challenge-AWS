
# import unittest
# from unittest.mock import patch, MagicMock
# from VisitCountFunc import app  # replace 'VisitCountFunc' with the name of your Python file

# class TestLambdaHandler(unittest.TestCase):
#     @patch('VisitCountFunc.app.table')
#     def test_lambda_handler(self, table_mock):
#         # Set up the mock object
#         get_item_response_mock = {'Item': {'id': '0', 'view_count': 1}}
#         table_mock.get_item.return_value = get_item_response_mock

#         # Run the function
#         result = app.lambda_handler({}, {})

#         # Assert the results
#         self.assertEqual(result, 2)
#         table_mock.get_item.assert_called_once_with(Key={'id': '0'})
#         table_mock.put_item.assert_called_once_with(Item={'id': '0', 'view_count': 2})

# if __name__ == '__main__':
#     unittest.main()

#####################################################################################

import unittest
from unittest.mock import patch, MagicMock
from VisitCountFunc import app  # replace 'VisitCountFunc' with the name of your Python file

# class TestLambdaHandler(unittest.TestCase):
#     @patch('VisitCountFunc.app.table')
#     def test_lambda_handler(self, table_mock):
#         # Set up the mock object
#         initial_view_count = 1
#         get_item_response_mock = {'Item': {'id': '0', 'view_count': initial_view_count}}
#         table_mock.get_item.return_value = get_item_response_mock

#         # Run the function
#         result = app.lambda_handler({}, {})

#         # Assert the results
#         self.assertEqual(result, initial_view_count + 1)
#         table_mock.get_item.assert_called_once_with(Key={'id': '0'})
#         table_mock.put_item.assert_called_once_with(Item={'id': '0', 'view_count': initial_view_count + 1})

#     @patch('VisitCountFunc.app.table')
#     def test_lambda_handler_no_initial_item(self, table_mock):
#         # Set up the mock object with no initial item
#         get_item_response_mock = {}
#         table_mock.get_item.return_value = get_item_response_mock

#         # Run the function
#         result = app.lambda_handler({}, {})

#         # Assert the results
#         self.assertEqual(result, 1)  # Assumes function initializes count to 1 if no initial item
#         table_mock.get_item.assert_called_once_with(Key={'id': '0'})
#         table_mock.put_item.assert_called_once_with(Item={'id': '0', 'view_count': 1})

# if __name__ == '__main__':
#     unittest.main()

############################################################################################
import sys
sys.path.insert(0, '../../VisitCountFunc')
import json
import unittest
from unittest.mock import patch, MagicMock
from VisitCountFunc import app  # replace 'VisitCountFunc' with the name of your Python file

class TestLambdaHandler(unittest.TestCase):
    @patch('VisitCountFunc.app.table')
    def test_lambda_handler(self, table_mock):
        # Set up the mock object
        initial_view_count = 1
        get_item_response_mock = {'Item': {'id': '0', 'view_count': initial_view_count}}
        table_mock.get_item.return_value = get_item_response_mock

        # Run the function
        response = app.lambda_handler({}, {})

        # Deserialize the response body
        result = json.loads(response['body'])

        # Assert the results
        # self.assertEqual(result, initial_view_count + 1)
        self.assertEqual(result['view_count'], initial_view_count + 1)
        table_mock.get_item.assert_called_once_with(Key={'id': '0'})
        table_mock.put_item.assert_called_once_with(Item={'id': '0', 'view_count': initial_view_count + 1})

    @patch('VisitCountFunc.app.table')
    def test_lambda_handler_no_initial_item(self, table_mock):
        # Set up the mock object with no initial item
        get_item_response_mock = {}
        table_mock.get_item.return_value = get_item_response_mock

        # Run the function
        response = app.lambda_handler({}, {})

        # Deserialize the response body
        result = json.loads(response['body'])

        # Assert the results
        # self.assertEqual(result, 1)  # Assumes function initializes count to 1 if no initial item
        self.assertEqual(result['view_count'], 1)
        table_mock.get_item.assert_called_once_with(Key={'id': '0'})
        table_mock.put_item.assert_called_once_with(Item={'id': '0', 'view_count': 1})

if __name__ == '__main__':
    unittest.main()
