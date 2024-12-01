from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Permit911
from customer.models import Customer
from .forms import E911PermitForm

def PermitHome(request):
    return render(request, 'permits/permithome.html')

def createE911Permit(request, pk=None):
    if pk:
        customer = get_object_or_404(Customer, pk=pk)
        if request.method == "POST":
            form = E911PermitForm(customer=customer, data=request.POST)
            if form.is_valid():
                permit = form.save(commit=False)
                permit.customer = customer
                permit.save()
                return redirect('permitlist')
        else:
            form = E911PermitForm(customer=customer)
        context = {
            'pk': pk,
            'customer': customer,
            'form': form
        }
    else:
        context = {}
    return render(request, 'permits/e911Permit.html', context)

def ClecoPermit(request):
    return render(request, 'permits/ClecoPermit.html')

def SwepcoPermit(request):
    return render(request, 'permits/SwepcoPermit.html')

class PermitList(ListView):
    model = Permit911
    template_name = 'permits/permitlist.html'
    context_object_name = 'permits'
    paginate_by = 10
    ordering = ['-permitdate', '-permittime']  # Show newest permits first

    def get_paginate_by(self, queryset):
        """Get the number of items to paginate by, from the request."""
        return self.request.GET.get('page_size', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
