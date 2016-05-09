from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Notification(models.Model):
    heading = models.CharField(max_length=200, null=True)
    description = models.TextField(blank = True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading
