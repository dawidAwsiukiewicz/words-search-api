# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from project.apps.search.managers import PageStatusObjectManager
from project.apps.utils.choices import PAGE_STATUS_CHOICES, page_status_started
from project.apps.utils.models import CreatedAbstract


class Page(CreatedAbstract):
    url = models.URLField(verbose_name=_(u"url"))
    status = models.SmallIntegerField(_(u"status"), choices=PAGE_STATUS_CHOICES, default=page_status_started)

    objects = PageStatusObjectManager()

    def __unicode__(self):
        return self.url

    class Meta:
        verbose_name = _(u"Strona")
        verbose_name_plural = _(u"Strony")


class Word(CreatedAbstract):
    page = models.ForeignKey("search.Page", verbose_name=_(u"Strona"))
    word = models.CharField(_(u"Słowo"), max_length=255)
    count = models.IntegerField(_(u"Liczba wystąpień"), default=0)

    class Meta:
        verbose_name = _(u"Słowo")
        verbose_name_plural = _(u"Słowa")

    def __unicode__(self):
        return "%s - %s" % (self.page, self.word)