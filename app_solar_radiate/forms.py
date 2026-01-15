from django.forms import ModelForm, TextInput
from app_solar_radiate.models import Data
from django import forms
from datetime import date

class DateForm(forms.Form):
        selected_date = forms.DateField(
            label='Выберите дату',
            widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            initial=date.today()
        )