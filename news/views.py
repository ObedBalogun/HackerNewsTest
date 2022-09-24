from django.views.generic import ListView, DetailView

from news.HackerAPI import HackerNews
from news.models import NewsItem


class NewsView(ListView):
    template_name = 'news_list.html'
    model = NewsItem
    paginate_by = 10

    def get_context_data(self, *, object_list=NewsItem.objects.all().order_by('-created'), **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        item_type = self.request.GET.get('type', None)
        search_title = self.request.GET.get('search', None)
        if item_type:
            object_list = object_list.filter(type=item_type)
            paginator = self.get_paginator(object_list, self.paginate_by)
            context['page_obj'] = paginator.page(1)
        if search_title:
            object_list = object_list.filter(text__icontains=search_title)
            paginator = self.get_paginator(object_list, self.paginate_by)
            context['page_obj'] = paginator.page(1)
        top_posts = NewsItem.objects.all().order_by('-score')[:5]
        context['top_posts'] = top_posts
        return context

class NewsDetailView(DetailView):
    template_name = 'news-detail.html'
    model = NewsItem
    slug_field = 'item_id'
    slug_url_kwarg = 'item_id'

    def get_context_data(self, *args, **kwargs):
        hacker = HackerNews()

        context = super(NewsDetailView,
                        self).get_context_data(**kwargs)
        news_item = NewsItem.objects.get(item_id=self.kwargs['item_id'])
        comments = news_item.kids
        comment_list = []
        if comments:
            for comment in comments:
                comment_details = hacker.get_news_details(comment)
                comment_list.append(comment_details)
        context['comments'] = comment_list
        context['news'] = news_item
        return context

