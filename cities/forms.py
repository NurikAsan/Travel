from django import forms
from .models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter name'
    }))

    class Meta:
        model = City
        fields = 'name',