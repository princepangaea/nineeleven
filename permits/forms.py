from django import forms
from django.forms import ModelForm
from .models import Permit911
from datetime import datetime


class Permit911Form(forms.ModelForm):
    permitdate = forms.DateField(widget=forms.SelectDateWidget(), label='permitdate', initial=datetime.today)
    permitnumber = forms.IntegerField()
    # permcompany = forms.ModelChoiceField()
    customer = forms.ChoiceField()
    permnewaddy = ()
    permaddymvdate = forms.DateField()
    class Meta:
        model = Permit911
        fields = '__all__'

'''
    category=forms.ModelChoiceField(
        label="",
        required=False,
        queryset=Category.objects.all(),
        empty_label="Select a category (optional)",
        widget=forms.Select(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Choose a category"
            }
        )
    )
    
    discord chris_calmatlas — Today at 8:58 PM'''    