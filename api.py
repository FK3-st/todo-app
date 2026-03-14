from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from todo.core import Todolist
from todo.storage import load, save



app = FastAPI()
todo = Todolist()

tasks, next_id = load()
todo.tasks = tasks
todo.next_id = next_id

class TaskInput(BaseModel):
    task: str

def save_todo():
    save(todo.tasks, todo.next_id)

@app.get("/tasks")
def get_tasks():
    return todo.list()

@app.post("/tasks")
def add_tasks(input: TaskInput):
    todo.add(input.task)
    save_todo()
    return {"message": "追加しました"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    try:
        todo.delete(task_id)
        save_todo()
        return {"message": "削除しました"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")


@app.patch("/tasks/{task_id}")
def done_task(task_id: int):
    try:
        todo.done(task_id)
        save_todo()
        return {"message": "達成しました"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")