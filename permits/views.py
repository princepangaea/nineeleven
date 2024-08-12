from django.shortcuts import render
from . import views

# Create your views here.
def PermitHome(request):
    context = {}
    return render(request, 'permits/permithome.html', context)

def E911Permit(request):
    context = {}
    return render(request, 'permits/e911Permit.html', context)

def ClecoPermit(request):
    context = {}
    return render(request, 'permits/e911Permit.html', context)

def SwepcoPermit(request):
    context = {}
    return render(request, 'permits/e911Permit.html', context)