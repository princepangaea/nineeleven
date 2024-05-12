from django.db import models

# Create your models here.

class Permit(models.Model):
    id = models.BigAutoField(primary_key=True)
    permitnumber = models.BigIntegerField(null=True)
    