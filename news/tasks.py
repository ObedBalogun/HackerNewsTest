import time
from celery import shared_task
from .helpers import *


@shared_task
def get_new_and_comment_asynchrously():
    fetch_news()
    resolve_comments()
    return "Done"
