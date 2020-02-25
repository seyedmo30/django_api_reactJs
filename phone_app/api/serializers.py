from django.contrib.auth.models import User
from rest_framework import serializers

from phone.models import Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = [
            'id',
            'name',
            'number',

        ]


class PhoneCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = [
            'name',
            'number',
            'group',
            'user'
        ]


class PhoneDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = [
            'id',
        ]
