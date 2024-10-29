from django.urls import path
from . import views
from address import urls
from permits import urls

urlpatterns = [
    path('customerlist', views.CustomerList, name='customerlist'),
    path('addcustomer', views.AddCustomer, name='addcustomer'),
    path('editcustomer/<int:cpk>', views.EditCustomer, name='editcustomer'),
    path('createcustomerpermit/<int:cpk>', views.CreateCustomerPermit, name='createcustomerpermit'),
    path('customerdetail/<int:cpk>', views.CustomerDetail, name='customerdetail'),
    path('search/', views.search, name='search'),
]
