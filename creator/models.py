from django.db import models

from utils.choices import PlatformChoices


class Creator(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    rating = models.DecimalField(max_digits=17, decimal_places=15)
    platform = models.PositiveSmallIntegerField(choices=PlatformChoices.choices)

    def __str__(self):
        return f"{self.name} ({self.username})"
