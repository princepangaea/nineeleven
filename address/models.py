from django.db import models
from django.forms import ModelForm
from customer.models import Customer
from django.utils.timezone import now

# Create your models here.
class ElectricProvider(models.Model):
        providername = models.CharField(max_length=255, null=True, blank=True)
        
        def __str__(self):
                return self.providername
                        
class WorkArea(models.Model):
        #WKAREA = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'11',12:'12',13:'13',14:'14',15:'15',16:'16',17:'17',18:'18',19:'19',20:'20',21:'21',22:'22',23:'23',24:'24',25:'25',26:'26',27:'27',28:'28',29:'29',}
        work_area_values = models.IntegerField(null=True)

        def __str__(self):
                return f'Work Area {self.work_area_values}'


class Address(models.Model):
        id = models.BigAutoField(primary_key=True)
        date_created = models.DateTimeField(auto_now_add=True)
        date_modified = models.DateTimeField(auto_now=True)
        housenum = models.IntegerField()
        aptnum = models.CharField(max_length=5, blank=True, null=True)
        lot_num = models.CharField(blank=True, null=True)
        street = models.CharField(max_length=255)
        city = models.CharField(max_length=100)
        STATE_CHOICES = (
                ("AL", "Alabama"),
                ("AK", "Alaska"),
                ("AZ", "Arizona"),
                ("AR", "Arkansas"),
                ("CA", "California"),
                ("CO", "Colorado"),
                ("CT", "Connecticut"),
                ("DE", "Delaware"),
                ("FL", "Florida"),
                ("GA", "Georgia"),
                ("HI", "Hawaii"),
                ("ID", "Idaho"),
                ("IL", "Illinois"),
                ("IN", "Indiana"),
                ("IA", "Iowa"),
                ("KS", "Kansas"),
                ("KY", "Kentucky"),
                ("LA", "Louisiana"),
                ("ME", "Maine"),
                ("MD", "Maryland"),
                ("MA", "Massachusetts"),
                ("MI", "Michigan"),
                ("MN", "Minnesota"),
                ("MS", "Mississippi"),
                ("MO", "Missouri"),
                ("MT", "Montana"),
                ("NE", "Nebraska"),
                ("NV", "Nevada"),
                ("NH", "New Hampshire"),
                ("NJ", "New Jersey"),
                ("NM", "New Mexico"),
                ("NY", "New York"),
                ("NC", "North Carolina"),
                ("ND", "North Dakota"),
                ("OH", "Ohio"),
                ("OK", "Oklahoma"),
                ("OR", "Oregon"),
                ("PA", "Pennsylvania"),
                ("RI", "Rhode Island"),
                ("SC", "South Carolina"),
                ("SD", "South Dakota"),
                ("TN", "Tennessee"),
                ("TX", "Texas"),
                ("UT", "Utah"),
                ("VT", "Vermont"),
                ("VA", "Virginia"),
                ("WA", "Washington"),
                ("WV", "West Virginia"),
                ("WI", "Wisconsin"),
                ("WY", "Wyoming"),
                )
        state = models.CharField(max_length=2, choices=STATE_CHOICES, default="LA")
        zip = models.CharField(max_length=10)
        customer = models.ForeignKey(to=Customer, on_delete=models.SET_NULL, null=True, blank=True)
        work_area_num = models.ForeignKey(to=WorkArea, on_delete=models.SET_NULL, null=True, blank=True)
        distance = models.IntegerField(null=True)
        origin = models.CharField(max_length=255)
        LORCHOICE = [("L","Left"), ("R","Right")]
        lr = models.CharField(max_length=1, choices=LORCHOICE, default="R")
        provider = models.ForeignKey(to=ElectricProvider, on_delete=models.SET_NULL, null=True, blank=True)
        notes = models.TextField(blank=True, null=True)

        def __str__(self):
                return f'{self.housenum} {self.aptnum} {self.street}'

        class Meta:
                verbose_name_plural = "Addresses"
                ordering = ["street","housenum"]
                