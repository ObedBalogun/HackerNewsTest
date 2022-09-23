from django.urls import path

from news.api_views import ListCreateNewsView, ListNewsDetail, ItemUpdateDestroyView
from news.views import NewsView, NewsDetailView

app_name = 'news'
urlpatterns = [
    path('api/', ListCreateNewsView.as_view()),
    path('api/<int:item_id>', ItemUpdateDestroyView.as_view()),

    path('list-news/', NewsView.as_view(), name='list-news'),
    path('news/<int:item_id>/', NewsDetailView.as_view(), name='news-detail'),
    ]