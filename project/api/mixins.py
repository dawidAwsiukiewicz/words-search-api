# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated


class UserAccessMixin(object):
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (IsAuthenticated,)


class PaginateConfig(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'per_page'
    max_page_size = 250


class PaginateMixin(object):
    pagination_class = PaginateConfig
