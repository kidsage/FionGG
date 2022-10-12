from django.db import models
import requests
from io import BytesIO

# Create your models here.
class UserDB(models.Model):
    nickname = models.CharField(max_length=10)
    access_ai = models.CharField(max_length=100)
    level = models.PositiveIntegerField(null=True)

    class Meta:
        db_table = 'UserDB'


class MatchDB(models.Model):
    matchtype = models.PositiveSmallIntegerField()
    desc = models.CharField(max_length=10)

    class Meta:
        unique_together = ('matchtype', 'desc')
        db_table = 'MatchDB'


class SpidDB(models.Model):
    sp_id = models.PositiveIntegerField()
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'SpidDB'


class ClassDB(models.Model):
    class_id = models.PositiveSmallIntegerField()
    class_name = models.CharField(max_length=100)
    class_img = models.CharField()

    class Meta:
        db_table = 'ClassDB'


class PositionDB(models.Model):
    spposition = models.PositiveSmallIntegerField()
    desc = models.CharField(max_length=10)

    class Meta:
        db_table = 'PositionDB'


class DivisionDB(models.Model):
    division_id = models.PositiveSmallIntegerField()
    division_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'DivisionDB'


class FaceonDB(models.Model):
    sp_id = models.ForeignKey(SpidDB, on_delete=models.CASCADE, null=True)
    p_id = models.PositiveIntegerField()
    division_name = models.ImageField(upload_to='images/player')

    class Meta:
        db_table = 'FaceonDB'