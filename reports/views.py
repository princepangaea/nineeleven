from django.shortcuts import render
from address.models import WorkArea


# Create your views here.
def ReportsHome(request):
    workareas = WorkArea.objects.all().order_by('work_area_values')
    context = {"workareas":workareas}
    return render(request, 'reports/reporthome.html', context)

def ReportsWorkArea(request, wka):
    context = {"wka":wka}
    return render(request, 'reports/workareas.html', context)

def WkAreaReport(request, wka):
    wkareport = WorkArea.objects.filter(wka).order_by('work_area_values')
    context = {}
    return render(request, 'reports/wkareareport.html', context)