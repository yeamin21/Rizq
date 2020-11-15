from django.db import models

from account.models import User
from restaurant.models import Food


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user')
    item = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.PositiveSmallIntegerField()

    def getTotal(self):
        return self.item.price * self.quantity

    def __str__(self):
        return self.item.name + " - " + str(self.quantity)


class Order(models.Model):
    orderItem = models.ManyToManyField(OrderItem)
    is_ordered = models.BooleanField(default=False)
    order_datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
