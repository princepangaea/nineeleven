from django.urls import path
from reports import views    

urlpatterns = [
    path('reportshome', views.ReportsHome, name = 'reportshome'),
    path('wkareport/<int:wka>', views.WkAreaReport, name = 'wkareareport')
]
