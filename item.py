from enum import Enum
from datetime import datetime

class Status(Enum):
    to_do = "To Do"
    doing = "Doing"
    done = "Done"

class ToDoItem:
    def __init__(self, id: str, title: str, status: Status, last_modified: datetime):
        self.id = id
        self.title = title
        self.status = status
        self.last_modified = last_modified