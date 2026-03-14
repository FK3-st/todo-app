class Todolist:

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add(self, task):
        new_task = {
            "id" :self.next_id,
            "task":task,
            "done":False
            }

        self.tasks.append(new_task)

        self.next_id += 1
        
    def list(self):
        return self.tasks

    def done(self,task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                return

        raise ValueError("Task not found")

    def delete(self, task_id):

        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return

        raise ValueError("Task not found")

    def search(self, keyword):
        return [task for task in self.tasks if keyword in task["task"]]
        



