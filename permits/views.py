from django.shortcuts import render
from . import views
from .forms import Permit911Form
from customer.models import Customer
from address.models import Address
from .models import Permit911
# Create your views here.

def PermitHome(request):
    context = {}
    return render(request, 'permits/permithome.html', context)

def E911Permit(request, cpk):
    customer = Customer.objects.get(id=cpk)
    
    # Check if a permit already exists for this customer
    permit = Permit911.objects.filter(customer=customer).first()
    
    if request.method == 'POST':
        form = Permit911Form(request.POST, instance=permit, customer=customer)
        if form.is_valid():
            form.save()
            return redirect('e911permit', cpk)
    else:
        form = Permit911Form(instance=permit, customer=customer)
    
    context = {'form': form, 'cpk': cpk}
    return render(request, 'permits/e911Permit.html', context)

'''
def E911Permit(request, cpk):
    currentpermit = Customer.objects.get(id=cpk)
    form = Permit911Form(request.POST or None, instance=currentpermit)
    if form.is_valid():
        form.save()
        return redirect('e911permit', cpk)
    context = {'form':form, 'cpk':cpk}
    return render(request, 'permits/e911Permit.html', context)
'''

'''def CreateCustomerPermit(request, cpk):
    currentcustomer = Customer.objects.get(id=cpk)
    form = CreatePermitfromCustomer(request.POST or None, instance=currentcustomer)
    if form.is_valid():
        form.save()
        return redirect('createcustomerpermit', cpk)
    context = {'form':form, 'cpk':cpk}
    return render(request, 'customer/createcustomerpermit.html', context)'''

def ClecoPermit(request):
    context = {}
    return render(request, 'permits/ClecoPermit.html', context)

def SwepcoPermit(request):
    context = {}
    return render(request, 'permits/SwepcoPermit.html', context)