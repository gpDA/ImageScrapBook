import celery
import thumbnail


if __name__ == "__main__":
    from time import sleep
    for x in range(100):
        thumbnail.add.delay(4, 4)
        sleep(1)
