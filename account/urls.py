from django.urls import path

from account import views
from account.views import CreateRestaurant, CreateCustomer

app_name = 'account'
urlpatterns = [
    path('register/restaurant', CreateRestaurant.as_view(), name='register-restaurant'),
    path('register/', CreateCustomer.as_view(), name='register'),
    # path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout')
]
