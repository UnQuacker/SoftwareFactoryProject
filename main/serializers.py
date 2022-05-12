import django_filters
from django.forms import CheckboxSelectMultiple
from rest_framework import serializers
from main.models import Place
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class PlaceSerializer(serializers.ModelSerializer, TaggitSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Place
        fields = ('id', 'name', 'tags', 'place_image', 'place_url')


# class CustomFilterList(django_filters.Filter):
#     def filter(self, qs, value):
#         if value not in (None, ''):
#             values = [v for v in value.split(',')]
#             return qs.filter(**{'%s__%s' % (self.name, self.lookup_type): values})
#         return qs
#
# class PropertyFilter(django_filters.FilterSet):
#     place = django_filters.ModelMultipleChoiceFilter(queryset=Place.objects.all(), widget = CheckboxSelectMultiple)
#     cities = CustomFilterList(name="city", lookup_type="in")
#
#     class Meta:
#         model = Place
#         fields = ['tags']