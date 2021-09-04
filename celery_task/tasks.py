import time
from celery import Celery

app = Celery('tasks', backend = 'redis://localhost', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    print("before execution %s, %s, %s"%(time.time(), x, y))
    z = x + y
    print("after execution %s, %s"%(time.time(), z))
    return z
