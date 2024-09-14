from django import forms
from django.forms import ModelForm
from .models import Permit911
from datetime import datetime
from customer.models import Customer
from address.models import Address

CUSTOMERS = Customer.first_name, Customer.last_name

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
        required=False
    )
    new_address = forms.ModelChoiceField(
        queryset=Address.objects.none(),
        label="New Address"
    )

    class Meta:
        model = Permit911
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super().__init__(*args, **kwargs)
        
        if customer:
            self.fields['customer'].initial = customer
            self.fields['customer_name'].initial = f"{customer.first_name} {customer.last_name}"
            # Fetch addresses related to this customer
            customer_addresses = Address.objects.filter(customer=customer)
            self.fields['current_address'].queryset = customer_addresses
            self.fields['new_address'].queryset = customer_addresses
            
            # Set initial value for current_address
            if customer_addresses.exists():
                self.fields['current_address'].initial = customer_addresses.first()
        else:
            self.fields['current_address'].queryset = Address.objects.none()
            self.fields['new_address'].queryset = Address.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        # Remove current_address from cleaned_data as it's not in the model
        cleaned_data.pop('current_address', None)
        return cleaned_data
        
'''
class Permit911Form(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.HiddenInput()
    )
    current_address = forms.ModelChoiceField(
        queryset=Customer.objects.none(),
        label="Current Address"
    )
    new_address = forms.ModelChoiceField(
        queryset=Customer.objects.none(),
        label="New Address"
    )

    class Meta:
        model = Permit911
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super().__init__(*args, **kwargs)
        
        if customer:
            self.fields['customer'].initial = customer
            self.fields['current_address'].queryset = customer.addresses.all()
            self.fields['new_address'].queryset = customer.addresses.all()
        else:
            self.fields['current_address'].queryset = Customer.objects.none()
            self.fields['new_address'].queryset = Customer.objects.none()
'''

'''class Permit911Form(forms.ModelForm):

    class Meta:
        model = Permit911
        fields = '__all__'
'''        

'''class Permit911Form(forms.ModelForm):
    permitdate = forms.DateField(widget=forms.SelectDateWidget(), label='permitdate', initial=datetime.today)
    permitnumber = forms.IntegerField()
    # permcompany = forms.ModelChoiceField()
    # customer = forms.ChoiceField( )
    permnewaddy = ()
    permaddymvdate = forms.DateField()
    class Meta:
        model = Permit911
        fields = '__all__'
'''        

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