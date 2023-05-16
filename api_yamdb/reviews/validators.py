from datetime import date

from rest_framework import serializers


def check_year(value):
    if value < 0 or value > date.today().year:
        raise serializers.ValidationError('Некорректно указан год')
