from django import forms
from .models import RestaurantDonation

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['fulfilled']