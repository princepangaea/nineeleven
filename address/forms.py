from django import forms
from .models import Address, ElectricProvider, WorkArea
from customer.models import Customer

class AddressForm(forms.ModelForm):
        housenum = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"House Number","label":"House Number", "class":"form-control form-control-sm col-sm-2"}), label="House No.")
        aptnum = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Apt. Number","label":"Apt. Number", "class":"form-control form-control-sm"}), label="Apt. No.")
        lot_num = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Lot Number","label":"Lot Number", "class":"form-control form-control-sm"}), label="Lot No.")
        street = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Street","label":"Street", "class":"form-control form-control-sm"}), label="Street")
        city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City","label":"City", "class":"form-control form-control-sm"}), label="City")
        STATE_CHOICES = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming",}
        state = forms.ChoiceField(required=True, choices=STATE_CHOICES.items(), widget=forms.Select(attrs={"placeholder":"State","label":"State", "class":"form-control form-control-sm"}), label="State", initial="LA")
        zip = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zip Code","label":"Zip Code", "class":"form-control form-control-sm"}), label="Zip Code")
        customer = forms.ModelChoiceField(required=False, queryset=Customer.objects.all(), widget=forms.HiddenInput())
        work_area_num = forms.ModelChoiceField(required=False, queryset=WorkArea.objects.all(), widget=forms.Select(attrs={"placeholder":"Work Area","label":"Work Area", "class":"form-control form-control-sm"}), label="Work Area")
        distance = forms.IntegerField(required=False, widget=forms.widgets.NumberInput(attrs={"placeholder":"","label":"Distance", "class":"form-control form-control-sm"}), label="Distance")
        origin = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Origin","label":"Origin", "class":"form-control form-control-sm"}), label="Origin")
        LORCHOICE = (("L", "Left"), ("R", "Right"))
        lr = forms.ChoiceField(required=True, choices=LORCHOICE, widget=forms.Select(attrs={"placeholder":"Left/Right","label":"Left/Right", "class":"form-control form-control-sm"}), label="Left/Right", initial="L")
        provider = forms.ModelChoiceField(required=False, queryset=ElectricProvider.objects.all(), widget=forms.Select(attrs={"placeholder":"Electric Provider","label":"Electric Provider", "class":"form-control form-control-sm"}), label="Electric Provider")
        notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder":"Notes","type":"textarea", "class":"form-control form-control-sm", "id":"inputEmail4"}), label="Notes")

        class Meta:
                model = Address
                fields = ['housenum','aptnum','street','city','state','zip','customer','work_area_num','distance','origin','lr','lot_num','provider','notes']
