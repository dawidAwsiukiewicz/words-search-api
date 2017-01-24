# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings

from .auth.views import LoginView, LogoutView
from .views import schema_view

urlpatterns = [
    # API ADMIN
    url(r'auth', LoginView.as_view(), name='auth'),
    url(r'logout', LogoutView.as_view(), name='logout'),
    url(r'^website/', include('project.api.website.urls', namespace='api_website')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^docs/', schema_view),
    ]
