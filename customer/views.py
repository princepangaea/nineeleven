from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Customer
from .forms import CustomerForm
from django.db.models import Q
from address.models import Address
import string

class CustomerList(ListView):
    model = Customer
    template_name = 'customer/customerlist.html'
    context_object_name = 'customers'
    ordering = ['last_name']
    paginate_by = 10

    def get_paginate_by(self, queryset):
        """Get the number of items to paginate by, from the request."""
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = super().get_queryset()
        letter = self.request.GET.get('letter', '')
        
        if letter and letter in string.ascii_uppercase:
            queryset = queryset.filter(last_name__istartswith=letter)
        
        return queryset.order_by('last_name', 'first_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all available first letters from customer last names
        available_letters = (
            Customer.objects.values_list('last_name', flat=True)
            .distinct()
            .order_by('last_name')
        )
        available_letters = sorted(set(name[0].upper() for name in available_letters if name))
        
        # Add all alphabet letters, marking which ones have customers
        alphabet = list(string.ascii_uppercase)
        context['letters'] = [
            {'letter': l, 'has_customers': l in available_letters}
            for l in alphabet
        ]
        context['current_letter'] = self.request.GET.get('letter', '')
        return context

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    addresses = Address.objects.filter(customer=customer).order_by('street', 'housenum')
    return render(request, 'customer/customerdetail.html', {
        'customer': customer,
        'addresses': addresses
    })

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('customerdetail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'customer/addcustomer.html', {'form': form})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save()
            return redirect('customerdetail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/editcustomer.html', {
        'form': form,
        'customer': customer
    })

def search_customers(request):
    query = request.GET.get('q')
    if query:
        results = Customer.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query)|
            Q(mailing_address__icontains=query)
        )
    else:
        results = []
    return render(request, 'customer/search_results.html', {
        'customers': results,
        'query': query
    })
