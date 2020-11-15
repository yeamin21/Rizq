from django.shortcuts import redirect
from django.views import generic

from cart.models import OrderItem, Order
from restaurant.models import Food


def addToCart(request, pk):
    item = OrderItem.objects.create(
        user=request.user,
        item=Food.objects.get(pk=pk),
        quantity=1
    )
    order, created = Order.objects.get_or_create(is_ordered=False, user=request.user)
    order.orderItem.add(item)
    if created:
        order.user = request.user
        order.save()
    return redirect('restaurant:home')


def updateCartItem(request, pk):
    item = OrderItem.objects.get(pk=pk)
    item.quantity = request.POST['quantity']
    item.save()
    return redirect('cart:list')


class ListOrder(generic.ListView):
    model = Order
    context_object_name = 'items'
    template_name = 'cart/cart.html'

    def get_queryset(self):
        return Order.objects.filter(is_ordered=False, user=self.request.user)
