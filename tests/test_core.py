from todo.core import Todolist
import pytest

@pytest.fixture
def todo():
    return Todolist()

def test_add_task(todo):

    todo.add("Python")

    tasks = todo.list()

    assert len(tasks) == 1
    assert tasks[0]["task"] == "Python"

@pytest.fixture
def todo_with_tasks(todo):
    todo.add("Python")
    todo.add("API")
    return todo

def test_done(todo_with_tasks):

    todo_with_tasks.done(1)

    tasks = todo_with_tasks.list()

    assert tasks[0]["done"] is True

def test_delete_task(todo_with_tasks):

    todo_with_tasks.delete(1)
    tasks = todo_with_tasks.list()

    assert len(tasks) == 1
    assert tasks[0]["task"] == "API"

def test_done_error(todo):

    with pytest.raises(ValueError):
        todo.done(1)

