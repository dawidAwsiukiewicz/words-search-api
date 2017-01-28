# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    class Meta:
        unique_together = ('email',)
        verbose_name = _(u"Użytkownik")
        verbose_name_plural = _(u"Użytkownicy")
