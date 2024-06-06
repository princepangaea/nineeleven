from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .models import Customer
from address.models import Address
from .forms import CustomerForm

# Create your views here.
def CustomerList(request):
    customer = Customer.objects.all
    context = {'customer':customer}
    return render(request, 'customer/customerlist.html', context)

def CustomerDetail(request, cpk):
    customer_detail = Customer.objects.get(id=cpk)
    custaddresses = Address.objects.filter(customer__id=cpk)
    context = {'customer_detail':customer_detail, 'cpk':cpk, 'custaddresses':custaddresses }
    return render(request, 'customer/customerdetail.html', context)

def EditCustomer(request, cpk):
    currentcustomer = Customer.objects.get(id=cpk)
    form = CustomerForm(request.POST or None, instance=currentcustomer)
    if form.is_valid():
        form.save()
        return redirect('customerdetail', cpk)
    context = {'form':form, 'cpk':cpk}
    return render(request, 'customer/editcustomer.html', context)

def AddCustomer(request):
    form = CustomerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid(): # type: ignore
            AddCustomer = form.save() # type: ignore
        return HttpResponseRedirect('customerlist')
    context = {'form':form}
    return render(request, 'customer/addcustomer.html', context)

