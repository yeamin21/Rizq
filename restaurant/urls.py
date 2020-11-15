from django.urls import path

from restaurant.views import ListFood, AddFood, AddLive, seeLive

app_name = 'restaurant'
urlpatterns = [
    #   path('food/',views.home,name='home'),
    path('', ListFood.as_view(), name='home'),
    path('add/', AddFood.as_view(), name='food-add'),
    path('go/', AddLive.as_view(), name='go-live'),
    path('live/<int:pk>',seeLive, name='see-live')
]
