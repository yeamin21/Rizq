from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from customer import forms
from customer.models import Order, OrderItem


class AddOrderView(CreateView):
    form_class = forms.AddToCartForm
    template_name = 'customer/add_food.html'
    model = OrderItem

    def form_valid(self, form):
        orderItem = form.save(commit=False)
        orderItem.user = self.request.user
        orderItem.save()
        return redirect('restaurant:home')


class OrderList(ListView):
    pass


class addToCart(CreateView):
    form_class = forms.CartForm
    template_name = 'customer/add_food.html'
    model = Order

    def form_valid(self, form):
        orderItem = form.save(commit=False)
        orderItem.user = self.request.user
        orderItem.save()
        return redirect('restaurant:home')


def removeFromCart(request):
    pass
