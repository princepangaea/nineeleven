from django.urls import path
from . import views

urlpatterns = [
    path('permithome', views.PermitHome, name='permithome'),
    path('e911permit/<int:cpk>', views.E911Permit, name='e911permit'),
    path('e911permit', views.E911Permit, name='e911permit'),
    path('clecopermit', views.ClecoPermit, name='clecopermit'),
    path('swepcopermit', views.SwepcoPermit, name='swepcopermit'),
]