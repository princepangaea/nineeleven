from django import forms
from address.models import Address, ElectricProvider, WorkArea
from .models import Customer


class CustomerForm(forms.ModelForm):    
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"First Name", "label":"First Name", "class":"form-control form-control-sm"}), label="First Name")
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Last Name", "label":"Last Name", "class":"form-control form-control-sm"}), label="Last Name")
    email = forms.EmailField()
    phone = forms.CharField()
    mailing_address = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Mailing Address", "label":"Mailing Address", "class":"form-control form-control-sm"}), label="Mailing Address")
    mailing_city = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"City", "label":"City", "class":"form-control form-control-sm"}), label="City")
    STATE_CHOICES = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming",}
    mailing_state = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=forms.Select(attrs={"placeholder":"State","label":"State", "class":"form-control form-control-sm"}), label="State", initial="LA")
    mailing_zip = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zip Code","label":"Zip Code", "class":"form-control form-control-sm"}), label="Zip Code")
   
    class Meta:
        model = Customer
        fields = ['first_name','last_name', 'email','phone','mailing_address','mailing_city','mailing_state','mailing_zip']


class CreatePermitfromCustomer(forms.ModelForm):    
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"First Name", "label":"First Name", "class":"form-control form-control-sm"}), label="First Name")
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Last Name", "label":"Last Name", "class":"form-control form-control-sm"}), label="Last Name")
    email = forms.EmailField()
    phone = forms.CharField()
    mailing_address = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Mailing Address", "label":"Mailing Address", "class":"form-control form-control-sm"}), label="Mailing Address")
    mailing_city = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"City", "label":"City", "class":"form-control form-control-sm"}), label="City")
    STATE_CHOICES = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming",}
    mailing_state = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=forms.Select(attrs={"placeholder":"State","label":"State", "class":"form-control form-control-sm"}), label="State", initial="LA")
    mailing_zip = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zip Code","label":"Zip Code", "class":"form-control form-control-sm"}), label="Zip Code")
   
    class Meta:
        model = Customer
        fields = ['first_name','last_name', 'email','phone','mailing_address','mailing_city','mailing_state','mailing_zip']


