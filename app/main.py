from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class TaskCreate(BaseModel):
    title: str


@app.get("/")
def read_root():
    return{"message": "API running"}

tasks = ["study docker", "build api"]

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(task: TaskCreate):
    tasks.append(task.title)
    return {"message": "Task added", "tasks": tasks}
