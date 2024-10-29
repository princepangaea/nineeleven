from django.urls import path
from . import views

urlpatterns = [
    path('permithome', views.PermitHome, name='permithome'),
    path('e911permit/<int:cpk>', views.createE911Permit, name='create911permit'),
    path('clecopermit', views.ClecoPermit, name='clecopermit'),
    path('swepcopermit', views.SwepcoPermit, name='swepcopermit'),
]
