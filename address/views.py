from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Address, ElectricProvider, WorkArea
from customer.models import Customer
from .forms import AddressForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def AddressList(request):
    workareaselect = WorkArea.objects.all()
    addresses = Address.objects.all()
    context = {'addresses':addresses, 'work_area':workareaselect}
    return render(request, 'address/addresslist.html', context)

def AddAddress(request, cpk=None):
    initial_data = {}
    customer = None
    
    if cpk is not None:
        try:
            customer = Customer.objects.get(id=cpk)
            initial_data['customer'] = customer
        except Customer.DoesNotExist:
            return render(request, 'error.html', {'message': 'Customer not found'})
    
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save()
            if customer:
                return redirect('customerdetail', cpk=cpk)
            return redirect('addresslist')
    else:
        form = AddressForm(initial=initial_data)
    
    context = {
        'form': form,
        'customer': customer,
        'cpk': cpk
    }
    return render(request, 'address/addaddress.html', context)

def EditAddress(request, apk):
    currentaddress = Address.objects.get(id=apk)
    form = AddressForm(request.POST or None, instance=currentaddress)
    if form.is_valid():
        form.save()
        return redirect('addressdetail', apk)
    context = {'form':form, 'apk':apk}
    return render(request, 'address/editaddress.html', context)

def AddressDetail(request, apk):
    address_detail = Address.objects.get(id=apk)
    context = {'address_detail':address_detail, 'apk':apk }
    return render(request, 'address/addressdetail.html', context)
