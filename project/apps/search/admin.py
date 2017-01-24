# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Page, Word


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass
