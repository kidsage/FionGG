from django.db import models

# Create your models here.
class UserInformation(models.Model):
    nickname = models.CharField(max_length=10)
    access_ai = models.CharField(max_length=100)
    level = models.PositiveIntegerField(null=True)


class Match(models.Model):
    pass


class Match(models.Model):
    pass


class Match(models.Model):
    pass