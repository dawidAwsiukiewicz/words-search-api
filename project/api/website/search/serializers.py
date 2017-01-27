# -*- coding: utf-8 -*-
import validators
from django.conf import settings
from project.apps.search.models import Page, Word
from project.apps.search.tasks import find_word
from rest_framework import serializers


class PageSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    words = serializers.CharField(required=True)
    bad_url_list = serializers.ReadOnlyField()

    class Meta:
        model = Page
        exclude = ('url',)

    def create(self, validated_data):
        request = self.context['request']
        data = request.data
        file = request.FILES['file']

        if file.content_type not in settings.ALLOWED_CONTENT_TYPE:
            raise serializers.ValidationError(u'Błędny typ pliku')

        bad_url_list = []
        words_list = data.get("words", None).split(",")

        for line in file.readlines():
            for url in line.split():
                if validators.url(url):
                    page_model = Page()
                    page_model.url = url
                    page_model.save()

                    for word in words_list:
                        if word:
                            word_model = Word()
                            word_model.page = page_model
                            word_model.word = word
                            word_model.save()
                    find_word.apply_async(args=[page_model])
                else:
                    bad_url_list.append(url)

        validated_data['bad_url_list'] = bad_url_list

        return validated_data


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        exclude = ()


class PageDetailSerializer(serializers.ModelSerializer):
    words = serializers.SerializerMethodField()
    status_display = serializers.ReadOnlyField(source="get_status_display")

    class Meta:
        model = Page
        exclude = ()

    def get_words(self, obj):
        return WordSerializer(obj.word_set.all(), many=True).data
