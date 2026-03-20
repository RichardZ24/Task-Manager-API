# Task-Manager-API
Simple FastAPI task manager API (in memory)

## How to run
```
uvicorn app.main:app --reload
```

## endpoints
```
GET /tasks
GET /tasks/{id}
POST /tasks
PUT /tasks/{id}
DELETE /tasks/{id}
GET /health
```

## Limitations
- In memory only, wil reset on restart.