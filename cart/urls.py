from django.urls import path

from cart.views import addToCart, ListOrder, updateCartItem

app_name = 'cart'
urlpatterns = [
    path('add/<int:pk>', addToCart, name='add'),
    path('list', ListOrder.as_view(), name='list'),
    path('update/<int:pk>', updateCartItem, name='update')
]
