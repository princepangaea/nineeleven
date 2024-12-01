from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Address, ElectricProvider, WorkArea
from customer.models import Customer
from .forms import AddressForm
import string

def index(request):
    return render(request, 'index.html')

class AddressList(ListView):
    model = Address
    template_name = 'address/addresslist.html'
    context_object_name = 'addresses'
    paginate_by = 10
    ordering = ['street', 'housenum']

    def get_paginate_by(self, queryset):
        """Get the number of items to paginate by, from the request."""
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = super().get_queryset()
        letter = self.request.GET.get('letter', '')
        
        if letter and letter in string.ascii_uppercase:
            queryset = queryset.filter(street__istartswith=letter)
        
        return queryset.order_by('street', 'housenum')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_area'] = WorkArea.objects.all()
        
        # Get all available first letters from street names
        available_letters = (
            Address.objects.values_list('street', flat=True)
            .distinct()
            .order_by('street')
        )
        available_letters = sorted(set(name[0].upper() for name in available_letters if name))
        
        # Add all alphabet letters, marking which ones have addresses
        alphabet = list(string.ascii_uppercase)
        context['letters'] = [
            {'letter': l, 'has_addresses': l in available_letters}
            for l in alphabet
        ]
        context['current_letter'] = self.request.GET.get('letter', '')
        return context

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
                return redirect('customerdetail', pk=cpk)
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
