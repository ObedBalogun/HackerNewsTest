from django.contrib import admin
from news.models import NewsItem,Comment

admin.site.register(NewsItem)
admin.site.register(Comment)