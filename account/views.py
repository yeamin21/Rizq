from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from account.forms import RestaurantCreationForm, CustomerCreationForm
from account.models import User


class CreateRestaurant(generic.CreateView):
    model = User
    template_name = 'account/register.html'
    form_class = RestaurantCreationForm

    def get_success_url(self):
        return reverse('account:login')


class CreateCustomer(generic.CreateView):
    model = User
    template_name = 'account/register.html'
    form_class = CustomerCreationForm

    def get_success_url(self):
        return reverse('account:login')


'''
class LoginPage(LoginView):
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_restaurant:
                print("REST")
                return redirect('restaurant:home')
            elif self.request.user.is_customer:
                print("CUST")
                return HttpResponse("THSTSS")
        return super(LoginPage,self).get(request,*args,**kwargs)
'''


def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_restaurant:
                login(request, user)
                return redirect('restaurant:home')
            elif user.is_customer:
                login(request, user)
                return redirect('restaurant:home')
    return render(request, 'account/login.html', {})


def logout_(request):
    logout(request)
    return redirect('restaurant:home')
