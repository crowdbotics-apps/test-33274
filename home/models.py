from django.conf import settings
from django.db import models


class Hall(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=256,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="hall_user",
    )


class Video(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=256,
    )
    url = models.URLField(
        null=True,
        blank=True,
    )
    youtube_id = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )
    hall = models.ForeignKey(
        "home.Hall",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="video_hall",
    )
