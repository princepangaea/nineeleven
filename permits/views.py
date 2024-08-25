from django.shortcuts import render
from . import views
from .forms import Permit911Form

# Create your views here.
def PermitHome(request):
    context = {}
    return render(request, 'permits/permithome.html', context)

def E911Permit(request):
    form = Permit911Form
    context = {'form':form}
    return render(request, 'permits/e911Permit.html', context)

def ClecoPermit(request):
    context = {}
    return render(request, 'permits/ClecoPermit.html', context)

def SwepcoPermit(request):
    context = {}
    return render(request, 'permits/SwepcoPermit.html', context)