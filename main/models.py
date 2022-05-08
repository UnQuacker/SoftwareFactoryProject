from django.db import models
from taggit.managers import TaggableManager


class Place(models.Model):
    name = models.CharField('place_name')
    tags = TaggableManager()

    def __str__(self):
        return self.name
