from rest_framework import serializers
from .models import *

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDB
        fields = ['nickname', 'access_id', 'level']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDB
        fields = ['matchtype', 'desc']


class SpidSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpidDB
        fields = ['sp_id', 'name']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDB
        fields = ['class_id', 'class_name', 'class_img']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionDB
        fields = ['spposition', 'desc']


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionDB
        fields = ['division_id', 'division_name']


class FaceonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDB
        fields = ['sp_id', 'p_id', 'faceon']