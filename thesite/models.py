from django.db import models
# Create your models here.


class Signup(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)


class UserDetails(models.Model):
    detailsId = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=10, null=False)
    place = models.CharField(max_length=100)


class Login(models.Model):
    email = models.EmailField(null=False)
    username = models.CharField(null=False, max_length=20)
    password = models.CharField(null=False, max_length=20)
