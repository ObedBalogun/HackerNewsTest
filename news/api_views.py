from django.views.generic import DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView, \
    get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

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

    def create(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "errors": serializer.errors
            })
        serializer.save()
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ItemUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    lookup_url_kwarg = 'item_id'

    def get_queryset(self):
        return NewsItem.objects.filter(from_api=True)

    def delete(self, request, *args, **kwargs):
        item = get_object_or_404(NewsItem, pk=kwargs['item_id'])
        if item.from_api:
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)


class ListNewsDetail(DetailView):
    model = NewsItem
    slug_field = 'item_id'
    slug_url_kwarg = 'item_id'

    def get_context_data(self, *args, **kwargs):
        hacker = HackerNews()
        context = super(ListNewsDetail,
                        self).get_context_data(**kwargs)
        news_item = NewsItem.objects.get(item_id=self.kwargs['item_id'])
        comments = news_item.kids
        comment_list = []
        for comment in comments:
            comment_details = hacker.get_news_details(comment)
            comment_list.append(comment_details)
        return comment_list

