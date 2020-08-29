import os
from requests import get, put, post, delete
import json
from item import ToDoItem, Status
from dateutil import parser

_todo_list=os.getenv('TODO_LIST_ID')
_doing_list=os.getenv('DOING_LIST_ID')
_done_list=os.getenv('DONE_LIST_ID')

_auth_params = {
    'key': os.getenv('API_KEY'),
    'token': os.getenv('USER_TOKEN')
}

def _make_item(trello_content, status):
    return ToDoItem(
        trello_content['id'],
        trello_content['name'],
        status,
        parser.parse(trello_content['dateLastActivity']))

def _get_list(list_id, category):
    response = get(f'https://api.trello.com/1/lists/{list_id}/cards', params=_auth_params)
    items = response.json()
    return [_make_item(content, category) for content in items]

def get_items():
    todo_items = _get_list(_todo_list, Status.to_do)
    doing_items = _get_list(_doing_list, Status.doing)
    done_items = _get_list(_done_list, Status.done)
    return todo_items + doing_items + done_items

def get_item(id):
    response = get(f'https://api.trello.com/1/cards/{id}', params=_auth_params)
    content = json.loads(response.content)
    status = Status.to_do if content['idList'] == _todo_list else Status.done
    return _make_item(content, status)

def add_item(title):
    card_details = {
        'name': title,
        'idList': _todo_list,
        'pos': 'bottom'
    }

    card_details.update(_auth_params)
    response = post('https://api.trello.com/1/cards', params=card_details)
    content = response.json()
    return _make_item(content, Status.to_do)

def mark_doing(id):
    list_details = {
        'idList': _doing_list
    }

    list_details.update(_auth_params)
    put(f'https://api.trello.com/1/cards/{id}', params=list_details)

def mark_done(id):
    list_details = {
        'idList': _done_list
    }

    list_details.update(_auth_params)
    put(f'https://api.trello.com/1/cards/{id}', params=list_details)


def create_trello_board():
    board_details = {
        'name': 'TEST_BOARD'
    }

    board_details.update(_auth_params)
    response = post(f'https://api.trello.com/1/boards/', params=board_details)
    content = response.json()
    return content['id']

def delete_trello_board(id):
    delete(f'https://api.trello.com/1/boards/{id}', params=_auth_params)


if __name__ == '__main__':
    new_item = add_item('testing testing')
    mark_done(new_item.id)
    todo_list = get_items()
    print(len(todo_list))