from django import forms

from restaurant.models import Food


class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ['restaurant']
