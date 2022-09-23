echo "--> Starting beats process"
celery -A hackernews beat --loglevel=info