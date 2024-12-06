from django.urls import path
from . import views
from address import urls

urlpatterns = [
    path('', views.index, name='index'),
    path('addresslist', views.AddressList.as_view(), name='addresslist'),
    path('addaddress', views.AddAddress, name='addaddress'),
    path('addaddress/<int:cpk>', views.AddAddress, name='addaddress_customer'),
    path('editaddress/<int:apk>', views.EditAddress, name='editaddress'),
    path('addressdetail/<int:apk>', views.AddressDetail, name='addressdetail')
]
