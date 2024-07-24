from django.db import models

from creator.models import Creator


class Content(models.Model):
    creator = models.ForeignKey('creator.Creator', on_delete=models.CASCADE, related_name='contents')
    url = models.URLField()

    def __str__(self):
        return f"{self.url} - from {self.creator.username}"

    @property
    def type(self):
        if self.url.lower().endswith('.mp4'):
            return 'video'
        else:
            return 'image'
