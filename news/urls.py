from django.urls import path

from news.api_views import ListCreateNewsView, ListNewsDetail

app_name = 'news'
urlpatterns = [
    path('', ListCreateNewsView.as_view(), name='index'),
    path('news/<int:item_id>', ListNewsDetail.as_view(), name='news'),
    ]