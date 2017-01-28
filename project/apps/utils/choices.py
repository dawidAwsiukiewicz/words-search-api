# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

page_status_started = 1
page_status_in_progess = 2
page_status_done = 3
page_status_error = 4

PAGE_STATUS_CHOICES = [
    (page_status_started, _(u'Rozpoczęty')),
    (page_status_in_progess, _(u'W trakcie')),
    (page_status_done, _(u'Zakończony')),
    (page_status_error, _(u'Problem z połączeniem')),
]