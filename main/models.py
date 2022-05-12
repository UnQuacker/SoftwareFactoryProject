from django.db import models
from taggit.managers import TaggableManager


class Place(models.Model):
    name = models.CharField('place_name', max_length=50)
    tags = TaggableManager()
    place_image = models.ImageField(null=True, blank=True, upload_to="images/")
    place_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
