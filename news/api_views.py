from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response

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


class ListNewsDetail(RetrieveAPIView):
    queryset = NewsItem.objects.prefetch_related()
    serializer_class = NewsSerializer
    permission_classes = permissions.AllowAny
