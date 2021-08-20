from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ToDo(models.Model):

    task = models.CharField(max_length=80, default='')
    finished = models.BooleanField(default=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

    def __str__(self):

        return _(self.task) or _('Tasks: %s') % ('finished' if self.finished else 'unfinished')
