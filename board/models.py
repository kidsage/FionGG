from django.db import models

# Create your models here.
class UserInformation(models.Model):
    nickname = models.CharField(max_length=10)



class Match(models.Model):
    pass