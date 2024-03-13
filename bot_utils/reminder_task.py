from celery import Celery

app = Celery(
    'reminder', broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
    )

app.conf.task_routes = {
    'app.tasks.*': {'queue': 'myqueue'}
}


@app.task
def send_notification():
    # тут логика работы с уведомлениями
    pass
