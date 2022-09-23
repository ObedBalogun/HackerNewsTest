echo "--> Starting worker process"
celery -A hackernews worker --loglevel=info -P eventlet
