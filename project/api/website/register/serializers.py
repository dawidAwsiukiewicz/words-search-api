# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext as _
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def create(self, validated_data):
        request = self.context['request']
        data = request.data
        validated_data['username'] = data.get("email")
        validated_data['email'] = data.get("email")
        validated_data['password'] = data.get("password")

        if validated_data.get('password'):
            validated_data['password'] = make_password(
                validated_data['password']
            )

        user, _created = get_user_model().objects.get_or_create(email=data.get("email"), username=data.get("email"), defaults={'password': validated_data['password']})
        if not _created:
            raise serializers.ValidationError(_(u'Użytkownik o taki adresie email już istnieje'))
        return user
