# -*- coding: utf-8 -*-
import re
import requests
from django.utils.html import strip_tags
from project.apps.utils.choices import page_status_in_progess, page_status_error, page_status_done
from project.celery import app


def clean_content(content):
    # remove JS
    pattern = re.compile(ur'<script[\s\S]+?/script>')
    content = re.sub(pattern, '', content)

    # remove css
    pattern = re.compile(ur'<style[\s\S]+?/style>')
    content = re.sub(pattern, '', content)

    # add space after tags
    content = content.replace(">", "> ")

    # striptags
    content = strip_tags(content)

    return content


@app.task(name='find_word')
def find_word(page):
    print u"## PAGE: %s was added to queue ##" % page.id
    page.status = page_status_in_progess
    page.save()
    try:
        request = requests.get(page.url)
    except:
        page.status = 4
        page.save()
        print u"!!~ PAGE: %s problem with request ~!!" % page.id
        return False

    content = clean_content(request.text)

    for word in page.word_set.all():
        if word.word in content:
            word.count = page_status_error
            word.save()

    page.status = page_status_done
    page.save()
    print u"## PAGE: %s DONE ##" % page.id
