from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Customer
from address.models import Address


# Create your views here.
def CustomerList(request):
    customer = Customer.objects.all
    context = {'customer':customer}
    return render(request, 'customer/customerlist.html', context)

def CustomerForm(request):
    context = {}
    return render(request, 'customer/customerform.html', context)

def CustomerDetail(request, cpk):
    customer_detail = Customer.objects.get(id=cpk)
    custaddresses = Address.objects.filter(customer__id=cpk)
    context = {'customer_detail':customer_detail, 'cpk':cpk, 'custaddresses':custaddresses }
    return render(request, 'customer/customerdetail.html', context)

'''
def CustomerDetail(request, cpk):
    customer_detail = Customer.objects.get(id=cpk)
    custaddresses = Address.objects.get(customer=customer_detail)
    context = {'customer_detail':customer_detail, 'cpk':cpk, 'custaddresses':custaddresses }
    return render(request, 'customer/customerdetail.html', context)
'''
'''
def CustomerDetail(request, cpk):
    customer = Customer.objects.get(Customer.id)
    customeraddresses = Address.objects.filter(customer)
    customer_detail = Customer.objects.get(id=cpk)
    context = {'customer_detail':customer_detail, 'cpk':cpk, 'customeradresses':customeraddresses }
    return render(request, 'customer/customerdetail.html', context)
'''
'''
# this one works
def CustomerDetail(request, cpk):
    customer_detail = Customer.objects.get(id=cpk)
    context = {'customer_detail':customer_detail, 'cpk':cpk }
    return render(request, 'customer/customerdetail.html', context)
'''

def AddCustomer(request):
    form = CustomerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid(): # type: ignore
            AddCustomer = form.save() # type: ignore
        return HttpResponseRedirect('customerlist')
    context = {'form':form}
    return render(request, 'customer/customerform.html', context)

