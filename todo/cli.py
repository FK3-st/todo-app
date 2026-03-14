import sys
from todo.core import Todolist
from todo.storage import load, save


todo = Todolist()
todo.tasks = load()

command = sys.argv[1]

if command == "add":

    task = sys.argv[2]
    todo.add(task)

elif command == "list":

    for i, task in enumerate(todo.list()):
        status = "x" if task["done"] else " "
        print(f"{i} [{status}] {task['task']}")

elif command == "done":

    task_id = int(sys.argv[2])
    todo.done(task_id)

save(todo.tasks)