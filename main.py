import sys
from todo.core import Todolist
from todo.storage import load, save

def main():
    todo = Todolist()
    
    tasks, next_id = load()
    todo.tasks = tasks
    todo.next_id = next_id

    command = sys.argv[1]

    if command == "add":

        task = sys.argv[2]
        todo.add(task)

    elif command == "list":

        for task in todo.list():

            status = "x" if task["done"] else " "
            print(f'{task["id"]}[{status}]"{task["task"]}')
    
    elif command == "done":

        task_id = int(sys.argv[2])
        todo.done(task_id)

    elif command == "delete":

        task_id = int(sys.argv[2])
        todo.delete(task_id)

    elif command == "search":

        keyword = sys.argv[2]
        
        for task in todo.search(keyword):

            status = "x" if task["done"] else " "
            print(f'{task["id"]}[{status}]"{task["task"]}')
    

    save(todo.tasks,todo.next_id)

if __name__ == "__main__":
    main()