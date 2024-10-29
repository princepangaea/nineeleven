from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Customer
from address.models import Address
from .forms import CustomerForm

def CustomerList(request):
    customers = Customer.objects.all().order_by('last_name', 'first_name')
    context = {'customer': customers}  # Keep as 'customer' to match template
    return render(request, 'customer/customerlist.html', context)

def AddCustomer(request):
    form = CustomerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            AddCustomer = form.save()
        return HttpResponseRedirect('customerlist')
    context = {'form':form}
    return render(request, 'customer/addcustomer.html', context)

def EditCustomer(request, cpk):
    currentcustomer = Customer.objects.get(id=cpk)
    form = CustomerForm(request.POST or None, instance=currentcustomer)
    if form.is_valid():
        form.save()
        return redirect('customerdetail', cpk)
    context = {'form':form, 'cpk':cpk}
    return render(request, 'customer/editcustomer.html', context)

def CustomerDetail(request, cpk):
    customer_detail = Customer.objects.get(id=cpk)
    custaddresses = Address.objects.filter(customer=cpk)
    context = {'customer_detail':customer_detail, 'custaddresses':custaddresses, 'cpk':cpk }
    return render(request, 'customer/customerdetail.html', context)

def CreateCustomerPermit(request, cpk):
    currentcustomer = Customer.objects.get(id=cpk)
    return redirect('create911permit', cpk=cpk)

def search(request):
    query = request.GET.get('q', '')
    
    if query:
        # Search in customers
        customers = Customer.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(mailing_address__icontains=query)
        ).order_by('last_name', 'first_name')
        
        # Search in addresses
        addresses = Address.objects.filter(
            Q(street__icontains=query) |
            Q(city__icontains=query) |
            Q(state__icontains=query) |
            Q(zip__icontains=query) |
            Q(housenum__icontains=query)
        ).order_by('street', 'housenum')
    else:
        customers = []
        addresses = []
    
    context = {
        'customers': customers,
        'addresses': addresses,
        'query': query
    }
    return render(request, 'customer/search_results.html', context)
