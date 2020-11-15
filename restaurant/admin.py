from django.contrib import admin

from account.models import Restaurant
from restaurant.models import Food, Live

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Live)
