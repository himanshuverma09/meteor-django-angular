from __future__ import absolute_import, unicode_literals

from dddp.api import API, Collection, Publication
from django_ddp_app import models


class Notification(Collection):
    model = models.Notification


class Notifications(Publication):
    queries = [
        models.Notification.objects.all().reverse(),
    ]

API.register([
    Notification,
    Notifications,
]);
