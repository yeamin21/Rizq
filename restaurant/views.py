from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import generic

from account.models import Restaurant
from restaurant.forms import AddFoodForm
from restaurant.models import Food, Live

'''
def home(request):
    return render(request,'restaurant/home.html',{})
'''


class ListFood(generic.ListView):
    model = Food
    context_object_name = 'foods'
    queryset = Food.objects.all()
    template_name = 'restaurant/food_list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_restaurant:
                return Food.objects.filter(restaurant=self.request.user)
            elif self.request.user.is_customer:
                return Food.objects.filter()
        else:
            return Food.objects.filter()


class AddFood(LoginRequiredMixin, generic.CreateView):
    form_class = AddFoodForm
    template_name = 'restaurant/add_food.html'

    def form_valid(self, form):
        food = form.save(commit=False)
        food.restaurant = self.request.user
        food.save()
        return redirect('restaurant:home')


def seeLive(request,pk):
    live= Live.objects.get(restaurant=pk)
    if live.is_active:
        split_url=str(live.url).split('/')
        video_key=split_url[-1]
        url='https://www.youtube.com/embed/'+video_key
    return render(request, template_name='Restaurant/live.html', context={
        'url':url
    })


class AddLive(generic.CreateView):
    template_name = 'Restaurant/live.html'
    model = Live
    fields = ['url']

    def form_valid(self, form):
        live = form.save(commit=False)
        live.restaurant = self.request.user
        live.is_active = True
        live.save()
