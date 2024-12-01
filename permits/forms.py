from django import forms
from .models import Permit911, Address

class E911PermitForm(forms.ModelForm):
    permnewaddy = forms.ModelChoiceField(
        queryset=Address.objects.none(),
        label="New Address",
        empty_label="Select new address",
        required=True
    )
    permoldaddy = forms.ModelChoiceField(
        queryset=Address.objects.none(),
        label="Current Address",
        empty_label="Select current address",
        required=False
    )

    class Meta:
        model = Permit911
        fields = ['permitdate', 'permitnumber', 'permcompany', 'permnewaddy', 'permoldaddy', 'permaddymvdate']
        widgets = {
            'permitdate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'permitnumber': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'permcompany': forms.Select(attrs={
                'class': 'form-control'
            }),
            'permaddymvdate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }
        labels = {
            'permitdate': 'Permit Date',
            'permitnumber': 'Permit Number',
            'permcompany': 'Electric Provider',
            'permaddymvdate': 'Move Date'
        }
    
    def __init__(self, customer=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if customer:
            # Filter address choices to only show addresses for this customer
            customer_addresses = Address.objects.filter(customer=customer)
            self.fields['permnewaddy'].queryset = customer_addresses
            self.fields['permoldaddy'].queryset = customer_addresses
            
            # Add Bootstrap classes to the address select fields
            self.fields['permnewaddy'].widget.attrs['class'] = 'form-control'
            self.fields['permoldaddy'].widget.attrs['class'] = 'form-control'
