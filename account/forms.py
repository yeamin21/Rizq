from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from account.models import User, Restaurant


class RestaurantCreationForm(UserCreationForm):
    location = forms.CharField(max_length=200)

    class Meta(UserCreationForm):
        model = User
        fields = ['username',
                  'email',
                  'location'
                  ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_restaurant = True
        user.is_active = False
        user.save()
        restaurant = Restaurant.objects.create(user=user)
        restaurant.location = self.cleaned_data.get('location')
        restaurant.save()
        return user


class CustomerCreationForm(UserCreationForm):
    # location = forms.CharField(max_length=200)

    class Meta(UserCreationForm):
        model = User
        fields = ['username',
                  'email',
                  # 'location'
                  ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        # user.is_restaurant = True
        user.save()
        # restaurant = restaurant.objects.create(user = user)
        # restaurant.location = self.cleaned_data.get('location')
        # restaurant.save()
        return user


class LoginForm(LoginView):
    class Meta:
        pass
