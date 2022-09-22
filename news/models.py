from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

# class NewsItemChildren(models.Model):
#     pass
NEWS_TYPES=(('news', 'News'), ('story', 'Story'), ('comment', 'Comment'),('job','Job'))

class NewsItem(models.Model):
    item_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=500)
    type = models.CharField(choices=NEWS_TYPES, max_length=10)
    score = models.IntegerField(default=0)
    url = models.URLField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    kids = ArrayField(models.IntegerField(default=0), default=list, null=True, blank=True)
    from_api = models.BooleanField(default=False)
    time_posted = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    commenter = models.CharField(max_length=100, null=True, blank=True)
    comment_id = models.IntegerField(default=0)
    parent_id = models.IntegerField(default=0)
    parent_article = models.ForeignKey(NewsItem, on_delete=models.CASCADE, related_name='comments', null=True,
                                       blank=True)
    text = models.TextField(null=True, blank=True)
    type = models.CharField(choices=(('news', 'News'), ('story', 'Story'), ('comment', 'Comment')), max_length=10)
    deep_comments = ArrayField(models.IntegerField(default=0), default=list, null=True, blank=True)
    timestamp = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


