from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_restaurant = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
