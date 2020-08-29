import os
from test_client import client
from unittest.mock import Mock, patch
import trello_items
import requests
import json

_todo_list=os.getenv('TODO_LIST_ID')
_doing_list=os.getenv('DOING_LIST_ID')
_done_list=os.getenv('DONE_LIST_ID')

def mock_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    url = args[0]

    if _todo_list in url:
        file_name = "to_do.json"
    elif _doing_list in url:
        file_name = "doing.json"
    elif _done_list in url:
        file_name = "done.json"

    file = open(f"test_data/{file_name}")
    return MockResponse(json.loads(file.read()), 200)

@patch.object(trello_items, 'get', side_effect=mock_requests)
def test_index_page(requests_mock, client):
    response = client.get('/')
    data = response.data.decode("utf-8")
    assert "Allow new items to be added" in data
    assert "You must do this" in data
    assert "I am doing this, honest guv" in data
    assert "This is a new item" in data
    assert "List saved todo items" in data
    assert "Done today" in data