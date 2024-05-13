from django.urls import path
from . import views
from address import urls

urlpatterns = [
    path('', views.index, name='index'),
    path('addresslist', views.AddressList, name='addresslist'),
    path('addaddress', views.AddAddress, name='addaddress'),
    path('editaddress/<int:apk>', views.EditAddress, name='editaddress'),
    path('addressdetail/<int:apk>', views.AddressDetail, name='addressdetail')
]