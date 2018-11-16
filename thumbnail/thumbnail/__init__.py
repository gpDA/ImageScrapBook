import celery


app = celery.Celery("thumbnail",
        broker='amqp://user:pass@rabbit:5672/vhost')


@app.task
def add(x, y):
    return x + y
