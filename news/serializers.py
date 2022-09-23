from django.db import IntegrityError
from rest_framework import serializers

from news.models import NewsItem


class NewsSerializer(serializers.ModelSerializer):
    pass

    def create(self, validated_data):
        try:
            news_item = NewsItem.objects.create(
                item_id=validated_data['item_id'],
                title=validated_data['title'],
                url=validated_data['url'],
                text=validated_data['text'],
                score=validated_data['score'],
                type=validated_data['type'],
                kids=validated_data['kids'],
                by=validated_data['by'],
                from_api=True,

            )
        except IntegrityError as e:
            raise serializers.ValidationError({"errors": str(e)}) from e

    class Meta:
        model = NewsItem
        fields = "__all__"
