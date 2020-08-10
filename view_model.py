from item import Status

class ViewModel:
    def __init__(self, items):
        self._items = items

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