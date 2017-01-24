# -*- coding: utf-8 -*-
from project.api.mixins import PaginateMixin, UserAccessMixin
from project.apps.search.models import Page
from rest_framework import mixins, viewsets
from .serializers import PageSerializer, PageDetailSerializer


class PageViewSet(
    UserAccessMixin,
    PaginateMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    model = Page
    queryset = model.objects.all().order_by("-id")
    serializer_class = PageSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = PageDetailSerializer
        return super(PageViewSet, self).list(request, *args, **kwargs)
