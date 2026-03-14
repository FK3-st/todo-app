import json
from pathlib import Path

FILE = Path("tasks.json")


def save(tasks, next_id):

    data = {
        "next_id" : next_id,
        "tasks" : tasks
    }
    
    with open(FILE, "w") as f:
        json.dump(data, f)

    if isinstance(data, list):
        return data, len(data) + 1

    return data["tasks"],data["next_id"]


def load():

    if not FILE.exists():
        return [], 1

    with open(FILE) as f:
        data = json.load(f)

    return data["tasks"], data["next_id"]

