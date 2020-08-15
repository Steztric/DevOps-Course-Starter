from item import Status, ToDoItem
from typing import List
from datetime import date

class ViewModel:
    def __init__(self, items: List[ToDoItem]):
        self._items = items
        self._show_all = True

    @property
    def items(self):
        return self._items

    @property
    def to_do(self):
        return list(filter(lambda x: x.status == Status.to_do, self._items))

    @property
    def doing(self):
        return list(filter(lambda x: x.status == Status.doing, self._items))

    @property
    def done(self):
        return list(filter(lambda x: x.status == Status.done, self._items))

    def recent_done_items(self, since_date: date):
        return list(filter(lambda x: x.status == Status.done and x.last_modified.date() >= since_date, self._items))

    @property
    def older_done_items(self):
        return self.done

    @property
    def show_all_done_items(self):
        return self._show_all

    @show_all_done_items.setter
    def show_all_done_items(self, value: bool):
        self._show_all = value