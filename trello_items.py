import os
from requests import get, put, post
import json
from item import ToDoItem

_todo_list='5f140cd74e0efa661d85d545'
_done_list='5f14102775f3e65db1615d81'

_auth_params = {
    'key': os.getenv('API_KEY'),
    'token': os.getenv('USER_TOKEN')
}

def _make_item(trello_content, status):
    return ToDoItem(trello_content['id'], trello_content['name'], status)

def _get_list(list_id, category):
    response = get(f'https://api.trello.com/1/lists/{list_id}/cards', params=_auth_params)
    items = json.loads(response.content)
    return [_make_item(content, category) for content in items]

def get_items():
    todo_items = _get_list(_todo_list, 'Not Started')
    done_items = _get_list(_done_list, 'Finished')
    return todo_items + done_items

def get_item(id):
    response = get(f'https://api.trello.com/1/cards/{id}', params=_auth_params)
    content = json.loads(response.content)
    status = "Not Started" if content['idList'] == _todo_list else "Finished"
    return _make_item(content, status)

def add_item(title):
    card_details = {
        'name': title,
        'idList': _todo_list,
        'pos': 'bottom'
    }

    card_details.update(_auth_params)
    response = post('https://api.trello.com/1/cards', params=card_details)
    content = json.loads(response.content)
    return _make_item(content, 'Not Started')

def mark_done(id):
    list_details = {
        'idList': _done_list
    }

    list_details.update(_auth_params)
    put(f'https://api.trello.com/1/cards/{id}', params=list_details)


if __name__ == '__main__':
    new_item = add_item('testing testing')
    mark_done(new_item.id)
    todo_list = get_items()
    print(len(todo_list))