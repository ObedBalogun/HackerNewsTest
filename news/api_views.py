from django.shortcuts import render
from django.views.generic import DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from news.HackerAPI import HackerNews
from news.models import NewsItem
from news.serializers import NewsSerializer


class BulkCreateNewsView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = NewsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)


class ListCreateNewsView(ListCreateAPIView):
    model = NewsItem
    serializer_class = NewsSerializer
    queryset = NewsItem.objects.prefetch_related()
    search_fields = ['text']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['type']
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'news_list.html'

    def create(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "errors": serializer.errors
            })
        serializer.save()
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return Response({'news': queryset})


class ListNewsDetail(DetailView):
    queryset = NewsItem.objects.prefetch_related()
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]
    slug_url_kwarg = "item_id"
    slug_field = "item_id"
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'news-detail.html'

    def get_context_data(self, **kwargs):
        hacker = HackerNews()
        context = super(ListNewsDetail, self).get_context_data(**kwargs)
        context['news'] = NewsItem.objects.get(item_id=self.kwargs['item_id'])
        comments = context['news'].kids
        comment_list = []
        for comment in comments:
            comment_details = hacker.get_news_details(comment)
            comment_list.append(comment_details)
        context['comments'] = comment_list
        return context
