import os
import time

from celery import Celery

CELERY_BROKER_URL = (os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),)
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

celery = Celery("tasks", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name="tasks.sum")
def sum(x: int, y: int) -> int:
    time.sleep(15)  # Very hard work ;-)
    return x + y
