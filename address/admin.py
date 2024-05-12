from django.contrib import admin
from . models import Address, ElectricProvider, WorkArea
# Register your models here.

admin.site.register(Address)
admin.site.register(ElectricProvider)
admin.site.register(WorkArea)