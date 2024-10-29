from django.shortcuts import render, redirect
from . import views
from .forms import Permit911Form
from customer.models import Customer
from address.models import Address
from .models import Permit911

def PermitHome(request):
    context = {}
    return render(request, 'permits/permithome.html', context)

def createE911Permit(request, cpk=None):
    if cpk is None:
        return render(request, 'permits/error.html', {'message': 'Customer ID is required'})

    try:
        customer = Customer.objects.get(id=cpk)
    except Customer.DoesNotExist:
        return render(request, 'permits/error.html', {'message': 'Customer not found'})
    
    # Check if a permit already exists for this customer
    permit = Permit911.objects.filter(customer=customer).first()
    
    if request.method == 'POST':
        form = Permit911Form(request.POST, instance=permit, customer=customer)
        if form.is_valid():
            form.save()  # The form's save method handles everything now
            return redirect('permithome')
    else:
        form = Permit911Form(instance=permit, customer=customer)
    
    context = {
        'form': form,
        'cpk': cpk,
        'customer': customer
    }
    return render(request, 'permits/e911Permit.html', context)

def ClecoPermit(request):
    context = {}
    return render(request, 'permits/ClecoPermit.html', context)

def SwepcoPermit(request):
    context = {}
    return render(request, 'permits/SwepcoPermit.html', context)
