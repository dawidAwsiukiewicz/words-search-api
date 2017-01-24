# -*- coding: utf-8 -*-

from django.db import models
from project.apps.utils.choices import page_status_done, page_status_in_progess, page_status_started


class PageStatusObjectQueryset(models.query.QuerySet):
    def started(self):
        return self.filter(status=page_status_started)

    def in_progress(self):
        return self.filter(status=page_status_in_progess)

    def done(self):
        return self.filter(status=page_status_done)


class PageStatusObjectManager(models.Manager):
    def get_queryset(self):
        return PageStatusObjectQueryset(self.model, using=self._db)

    def started(self):
        return self.get_queryset().started()

    def in_progress(self):
        return self.get_queryset().in_progress()

    def done(self):
        return self.get_queryset().done()
