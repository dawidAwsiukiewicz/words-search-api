# -*- coding: utf-8 -*-
__author__ = 'Dawid Awsiukiewicz'

from rest_framework import routers
import views

router = routers.SimpleRouter()
router.register(r'register', views.RegisterViewSet)
urlpatterns = router.urls