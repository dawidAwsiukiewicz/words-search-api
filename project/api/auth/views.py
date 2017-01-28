# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth import logout
from django.utils.translation import ugettext as _
from project.apps.accounts.models import CustomUser
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserAuthTokenSerializer


class LoginView(APIView):
    def auth_with_data(self, data):
        serializer = UserAuthTokenSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data['username']
            user_data = {}
            user_data['username'] = user.username
            user_data['name'] = user.get_full_name()
            token, created = Token.objects.get_or_create(user=serializer.validated_data['username'])
            return Response({'token': token.key, 'user_data': user_data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        return self.auth_with_data(request.data or request.query_params)

    def get_queryset(self):
        return CustomUser.objects.all()


class LogoutView(APIView):
    def post(self, request):
        if not settings.DEBUG:
            try:
                request.user.auth_token.delete()
            except:
                pass

        logout(request)

        return Response({"success": _(u"Wylogowano poprawnie.")},
                        status=status.HTTP_200_OK)
