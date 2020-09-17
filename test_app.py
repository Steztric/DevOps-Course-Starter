import os
from threading import Thread
import app
import pytest
import trello_items
from contextlib import contextmanager
import dotenv
from pathlib import Path

def create_trello_board():
    board_id = trello_items.create_trello_board('Temporary Board')
    os.environ['TODO_LIST_ID'] = trello_items.create_trello_list('To do', board_id)
    os.environ['DOING_LIST_ID'] = trello_items.create_trello_list('Doing', board_id)
    os.environ['DONE_LIST_ID'] = trello_items.create_trello_list('Done', board_id)
    return board_id

@pytest.fixture(scope='module')
def test_app():
    env_path = Path('.') / '.env'
    dotenv.load_dotenv(dotenv_path=env_path)

    # Create a temporary board
    board_id = create_trello_board()

    # construct the new application
    application = app.create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app

    # Tear Down
    thread.join(1)
    trello_items.delete_trello_board(board_id)