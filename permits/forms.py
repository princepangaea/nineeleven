from django import forms
from . models import Permit911

class Permit911Form(forms.ModelForm):
    permitdate = forms.DateField()
    permitnumber = forms.IntegerField()
    permcompany = forms.ModelChoiceField()
    customer = forms.ChoiceField()
    permnewaddy = ()
    permoldaddy = ()
    permaddymvdate = forms.DateField(initial=datetime.date.today)

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