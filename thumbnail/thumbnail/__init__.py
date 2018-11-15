import celery


app = celery.Celery("thumbnail",
        broker='amqp://user:pass@rabbit:5672/vhost')


@app.task
def add(x, y):
    return x + y


if __name__ == "__main__":
    from time import sleep
    for x in range(100):
        add.delay(4, 4)
        sleep(1)

