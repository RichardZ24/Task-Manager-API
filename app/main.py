from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "API running"}

@app.get("/tasks")
def get_tasks():
    return {"tasks":[]}