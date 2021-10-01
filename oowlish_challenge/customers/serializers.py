# coding: utf-8
from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('__all__')

    def get_gender(self,obj):
        return obj.get_gender_display()
