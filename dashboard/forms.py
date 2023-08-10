from django import forms
from django.forms import ModelForm
from .models import Surfaceproducts
from bootstrap_datepicker_plus.widgets import DatePickerInput



class surface_form(forms.ModelForm):
    ht= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"ht","class":"field-style field-split align-left"}), max_length=100, required=True)
    dia= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"dia","class":"field-style field-split align-right"}), max_length=100, required=True)
    spring_dia= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"spring_dia","class":"field-style field-split align-left"}), max_length=1000, required=True)
    material=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"material","class":"field-style field-split align-right"}), max_length=100, required=True)
    pitch=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"pitch","class":"field-style field-split align-left"}), max_length=1000, required=True)
    value=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Value",'value':"material","class":"field-style field-split align-right"}), max_length=100, required=True)
    class Meta:
        model = Surfaceproducts
        fields = ["ht","dia","spring_dia","material","pitch","value"]
