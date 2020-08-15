from view_model import ViewModel
from item import ToDoItem, Status
from datetime import datetime, date

test_data = [
    ToDoItem('1', 'One', Status.to_do, datetime(2020, 8, 11)),
    ToDoItem('2', 'Two', Status.doing, datetime(2020, 8, 11)),
    ToDoItem('3', 'Three', Status.done, datetime(2020, 8, 11))
]

def test_to_do_works_with_no_items():
    assert ViewModel([]).to_do == []

def test_to_do_returns_only_items_to_do():
    view_model = ViewModel(test_data)
    items = view_model.to_do
    assert len(items) == 1
    assert items[0].id == '1'

def test_doing_returns_only_items_doing():
    view_model = ViewModel(test_data)
    items = view_model.doing
    assert len(items) == 1
    assert items[0].id == '2'

def test_done_returns_only_items_done():
    view_model = ViewModel(test_data)
    items = view_model.done
    assert len(items) == 1
    assert items[0].id == '3'

def test_show_all_done_items_defaults_true():
    view_model = ViewModel(test_data)
    assert view_model.show_all_done_items == True

def test_show_all_done_items_can_be_set():
    view_model = ViewModel(test_data)
    view_model.show_all_done_items = False
    assert view_model.show_all_done_items == False

def test_recent_done_items_returns_only_todays_done_items():
    inputs = [
        ToDoItem('1', 'One', Status.done, datetime(2020, 1, 1)),
        ToDoItem('2', 'Two', Status.done, datetime(2020, 5, 1)),
        ToDoItem('3', 'Three', Status.done, datetime(2020, 5, 1))
    ]
    today = date(2020, 5, 1)
    view_model = ViewModel(inputs)
    items = view_model.recent_done_items(today)
    assert list(map(lambda x: x.id, items)) == ['2', '3']
