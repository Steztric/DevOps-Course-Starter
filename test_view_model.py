from view_model import ViewModel
from item import ToDoItem, Status

test_data = [
    ToDoItem('1', 'One', Status.to_do),
    ToDoItem('2', 'Two', Status.doing),
    ToDoItem('3', 'Three', Status.done)
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
