# -*- coding: utf-8 -*-
from project.apps.search.models import Page, Word
from rest_framework import serializers


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        exclude = ()


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        exclude = ()


class PageDetailSerializer(serializers.ModelSerializer):
    words = serializers.SerializerMethodField()

    class Meta:
        model = Page
        exclude = ()

    def get_words(self, obj):
        return WordSerializer(obj.word_set.all(), many=True)
