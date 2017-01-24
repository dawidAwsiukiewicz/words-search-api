# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate

from django.utils.translation import ugettext as _
from rest_framework import exceptions, serializers


class UserAuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    msg = _(u'To konto zostało wyłączone')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _(u"Zły login lub hasło")
                raise exceptions.ValidationError(msg)
        else:
            msg = _(u"Zły login lub hasło")
            raise exceptions.ValidationError(msg)

        attrs['username'] = user
        return attrs
