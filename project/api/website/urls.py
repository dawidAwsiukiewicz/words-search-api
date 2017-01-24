# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'search/', include('project.api.website.search.urls', namespace="search")),

]
