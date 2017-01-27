# -*- coding: utf-8 -*-
import requests
from project.celery import app

@app.task(name='find_word')
def find_word(page):
    r = requests.get("http://zadluzenia.com")
    r.text
