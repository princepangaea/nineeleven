from django.urls import path
from . import views
from address import urls

urlpatterns = [
    path('customerlist', views.CustomerList, name='customerlist'),
    path('addcustomer', views.AddCustomer, name='addcustomer'),
    path('customerdetail/<int:cpk>', views.CustomerDetail, name='customerdetail')
]