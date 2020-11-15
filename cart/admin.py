from django.contrib import admin

from cart.models import OrderItem, Order

admin.site.register(OrderItem)
admin.site.register(Order)
