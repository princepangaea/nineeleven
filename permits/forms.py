from django import forms
from django.forms import ModelForm
from .models import Permit911
from datetime import datetime
from customer.models import Customer
from address.models import Address, ElectricProvider

class Permit911Form(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.HiddenInput())
    customer_name = forms.CharField(
        label="Customer Name",
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}
    ))
    current_address = forms.ModelChoiceField(
        queryset=Address.objects.none(),
        label="Current Address",
        required=True
    )
    new_address = forms.ModelChoiceField(
        queryset=Address.objects.none(),
        label="New Address",
        required=False
    )
    permitdate = forms.DateField(
        initial=datetime.today,
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    permitnumber = forms.IntegerField(required=True)
    permcompany = forms.ModelChoiceField(
        queryset=ElectricProvider.objects.all(),
        label="Electric Provider",
        required=True
    )
    permaddymvdate = forms.DateField(
        label="Move Date",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = Permit911
        fields = ['permitdate', 'permitnumber', 'permcompany', 'permaddymvdate', 'customer', 'permnewaddy', 'permoldaddy']

    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super().__init__(*args, **kwargs)
        
        if customer:
            self.fields['customer'].initial = customer
            self.fields['customer_name'].initial = f"{customer.first_name} {customer.last_name}"
            
            # Get all addresses for this customer
            customer_addresses = Address.objects.filter(customer=customer)
            
            # Update the querysets for both address fields
            self.fields['current_address'] = forms.ModelChoiceField(
                queryset=customer_addresses,
                label="Current Address",
                required=True
            )
            self.fields['new_address'] = forms.ModelChoiceField(
                queryset=customer_addresses,
                label="New Address",
                required=False
            )
            
            # Set initial values if addresses exist
            if customer_addresses.exists():
                self.fields['current_address'].initial = customer_addresses.first()

    def clean(self):
        cleaned_data = super().clean()
        # Map the address fields to their model counterparts
        if 'new_address' in cleaned_data:
            cleaned_data['permnewaddy'] = cleaned_data.pop('new_address')
        if 'current_address' in cleaned_data:
            cleaned_data['permoldaddy'] = cleaned_data.pop('current_address')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Ensure the addresses are properly set
        if hasattr(self, 'cleaned_data'):
            if 'permnewaddy' in self.cleaned_data:
                instance.permnewaddy = self.cleaned_data['permnewaddy']
            if 'permoldaddy' in self.cleaned_data:
                instance.permoldaddy = self.cleaned_data['permoldaddy']
        if commit:
            instance.save()
        return instance
