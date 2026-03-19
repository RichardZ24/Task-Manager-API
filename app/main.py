from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class TaskCreate(BaseModel):
    title: str

class Task(BaseModel):
    title: str
    id: int
    completed: bool

class TaskCompletion(BaseModel):
    id: int
    completed: bool

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
    tasks.append(Task(title = task.title, id = new_task_id, completed = False))
    return {"message": "Task added", "tasks": tasks}

@app.put("/tasks/id")
def update_task_completion(task: TaskCompletion):
    target_id = task.id
    new_state = task.completed
   
    for stored_task in tasks:

        if (target_id != stored_task.id):
            continue

        if (new_state == stored_task.completed):
            return {"message" : f"Task is already marked as {"complete" if (new_state == True) else "incomplete"}.", "tasks:": tasks}
        
        stored_task.completed = new_state
        return {"message" : f"Task is marked as {"complete" if (new_state == True) else "incomplete"}", "tasks": tasks}
    return {"message" : "Task was not found, please enter a valid task id.", "tasks" : tasks}
    


