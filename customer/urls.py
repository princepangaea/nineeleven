from django.urls import path
from . import views
from address import urls
from permits import urls

urlpatterns = [
    path('customerlist/', views.CustomerList.as_view(), name='customerlist'),
    path('addcustomer/', views.add_customer, name='addcustomer'),
    path('editcustomer/<int:pk>/', views.edit_customer, name='editcustomer'),
    path('customerdetail/<int:pk>/', views.customer_detail, name='customerdetail'),
    path('search/', views.search_customers, name='search'),
]
