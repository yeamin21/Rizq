from django.db import models

from account.models import Restaurant, User


class Food(models.Model):
    if User.is_restaurant:
        restaurant = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=50)
        price = models.DecimalField(max_digits=7, decimal_places=2)
        image = models.ImageField(upload_to='images/food')

    def __str__(self):
        return self.name


class Live(models.Model):
    url = models.URLField()
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
