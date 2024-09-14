from django.db import models
from customer.models import Customer
from address.models import ElectricProvider, Address


# Create your models here.

class Permit911(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.DO_NOTHING)
    permittime = models.DateTimeField(auto_now_add=True)
    permitdate = models.DateField()
    permitnumber = models.BigIntegerField(null=True)
    permcompany = models.ForeignKey(to=ElectricProvider, on_delete=models.DO_NOTHING)
    permnewaddy = models.ForeignKey(Address, related_name='pnewaddress', on_delete=models.DO_NOTHING)
    permoldaddy = models.ForeignKey(Address, related_name='poldaddress', on_delete=models.DO_NOTHING, default=None)
    permaddymvdate = models.DateField(max_length=25) #move date on permit
    