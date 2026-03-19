from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class TaskCreate(BaseModel):
    title: str

class Task(BaseModel):
    title: str
    id: int

@app.get("/")
def read_root():
    return{"message": "API running"}

tasks = []

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(task: TaskCreate):
    if not tasks:
        new_task_id = 1
    else:
        new_task_id = tasks[-1].id + 1
    tasks.append(Task(title = task.title, id = new_task_id))
    return {"message": "Task added", "tasks": tasks}
