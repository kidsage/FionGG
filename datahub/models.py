from django.db import models
import requests
from io import BytesIO

# Create your models here.
class UserInformation(models.Model):
    nickname = models.CharField(max_length=10)
    access_ai = models.CharField(max_length=100)
    level = models.PositiveIntegerField(null=True)


class MatchDB(models.Model):
    matchtype = models.PositiveSmallIntegerField()
    desc = models.CharField(max_length=10)

    class Meta:
        unique_together = ('matchtype', 'desc')


class SpidDB(models.Model):
    spid = models.PositiveIntegerField()
    name = models.CharField(max_length=30)


class ClassDB(models.Model):
    class_id = models.PositiveSmallIntegerField()
    class_name = models.CharField(max_length=100)
    class_img = models.CharField()


class PositionDB(models.Model):
    spposition = models.PositiveSmallIntegerField()
    desc = models.CharField(max_length=10)


