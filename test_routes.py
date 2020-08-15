from test_client import client
from unittest.mock import Mock, patch
import trello_items
import requests

def mock_requests():
    mock = Mock()
    mock.configure_mock(return_value=True)
    return mock

@patch.object(requests, 'get', side_effect=mock_requests)
def test_index_page(requests_mock, client):
    response = client.get('/')
    assert response == True