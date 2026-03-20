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
    completed: bool

@app.get("/")
def read_root():
    return{"message": "API running"}

@app.get("/health")
def health_check():
    return {"status" : "ok"}

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
    new_task = Task(title = task.title, id = new_task_id, completed = False)
    tasks.append(new_task)
    return {"message": "Task added", "task": new_task}

@app.put("/tasks/{id}")
def update_task_completion(id: int, task: TaskCompletion):
    new_state = task.completed
   
    for stored_task in tasks:

        if (id != stored_task.id):
            continue

        if (new_state == stored_task.completed):
            return {"message" : f"Task is already marked as {'complete' if (new_state) else 'incomplete'}.", "updated task": stored_task}
        
        stored_task.completed = new_state
        return {"message" : f"Task is marked as {'complete' if (new_state) else 'incomplete'}", "updated task": stored_task}
    return {"message" : "Task was not found, please enter a valid task id."}
    

@app.delete("/tasks/{id}")
def delete_task(id: int):
    # index based for loop for good practise when modifying a looping list. (unecessary for this instance)
    
    for i, stored_task in enumerate(tasks):
        if (id == stored_task.id):
            old_task  = tasks[i]
            tasks.pop(i)
            return {"message" : "Task successfully removed", "task" : old_task }
    return {"message" : "Task not found"}


@app.get("/tasks/{id}")
def get_task(id: int):
    for stored_task in tasks:
        if (id == stored_task.id):
            return {"task" : stored_task}
    return {"message" : "Task not found"}