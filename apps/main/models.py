from django.db import models

from ..apps_utils.base_model import CUDateModel


class Announcement(models.Model, CUDateModel):
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name
