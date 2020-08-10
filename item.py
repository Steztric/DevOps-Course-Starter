from enum import Enum

class Status(Enum):
    to_do = "To Do"
    doing = "Doing"
    done = "Done"

class ToDoItem:
    def __init__(self, id: str, title: str, status: Status):
        self.id = id
        self.title = title
        self.status = status