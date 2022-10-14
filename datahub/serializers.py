import inspect
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from django.utils.translation import ugettext_lazy as _
from .models import *

#
## test code
class BulkSerializer(serializers.ListSerializer):

    def update(self, queryset, validated_data):
        id_attr = getattr(self.child.Meta, 'update_lookup_field')
        update_data = {i.get(id_attr): i for i in validated_data}

        if not all((bool(i) and not inspect.isclass(i) for i in update_data.keys())):
            raise NotFound(_('Could not find all objects to update.'))

        objects = queryset.filter(**{'{}__in'.format(id_attr): update_data.keys()})

        if len(update_data) != objects.count():
            raise NotFound(_('Could not find all objects to update.'))

        ret = []
        for id, data in update_data.items():
            for obj in objects:
                if str(getattr(obj, id_attr)) == str(id):
                    ret.append(self.child.update(obj, data))

        return ret
##


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDB
        fields = ['nickname', 'access_id', 'level']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDB
        fields = ['matchtype', 'desc']
        list_serializer_class = BulkSerializer


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