from django.db import models
from customer.models import Customer
from address.models import ElectricProvider, Address


# Create your models here.

class Permit911(models.Model):
    id = models.BigAutoField(primary_key=True)
    permittime = models.DateTimeField(auto_now_add=True)
    permitdate = models.DateField()
    permitnumber = models.BigIntegerField(null=True)
    permcompany = models.ForeignKey(to=ElectricProvider, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(to=Customer, on_delete=models.DO_NOTHING)
    permnewaddy = models.ForeignKey(Address, related_name='pnewaddress', on_delete=models.DO_NOTHING)
    permoldaddy = models.ForeignKey(Address, related_name='poldaddress', on_delete=models.DO_NOTHING, default=None)
    permaddymvdate = models.TextField(max_length=25) #move date on permit

    
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