import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackernews.settings')

app = Celery('hackernews')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'get-new-and-comments-every-five-min': {
        'task': 'news.tasks.get_new_and_comment_asynchronously',
        'schedule': crontab(minute='*/5')
    }
}