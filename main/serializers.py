from rest_framework import serializers
from main.models import Place
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class PlaceSerializer(serializers.ModelSerializer, TaggitSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Place
        fields = ('id', 'name', 'tags')
