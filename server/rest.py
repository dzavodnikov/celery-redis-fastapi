import os

import celery.states as states
from celery import Celery
from fastapi import FastAPI, Query

CELERY_BROKER_URL = (os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),)
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


app = FastAPI()
celery = Celery("tasks", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@app.post("/sum", description="Sum two values in Celery task.")
async def add(
    a: int = Query(None, description="First value", example=1),
    b: int = Query(None, description="Second value", example=2),
) -> str:
    task = celery.send_task("tasks.sum", args=[a, b], kwargs={})
    return task.id


@app.get("/result", description="Get result of Celery task.")
async def check_task(task_id: str = Query(None, description="Task ID")) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)
