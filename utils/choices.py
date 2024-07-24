from django.db import models


class PlatformChoices(models.IntegerChoices):
    INSTAGRAM = 1, 'Instagram'
    TIKTOK = 2, 'TikTok'
    UGC = 3, 'User Generated Content'
