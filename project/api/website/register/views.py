# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from .serializers import UserSerializer


class RegisterViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    model = get_user_model()
    queryset = model.objects.all().order_by("-id")
    serializer_class = UserSerializer
