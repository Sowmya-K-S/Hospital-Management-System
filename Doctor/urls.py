from django.urls import path
from Doctor.views import *

urlpatterns = [
"""    path('', index_view, name='d_index.htm
    path('register/', register_view, name="d_register.html"),
    path('login/', login_view, name="d_login.html"),
    path('otp/', otp_view, name="seller_otp"),
    path('logout/', logout_view, name='seller_logout'),
    path('add_product/', add_product, name='add_product'),
    path('inventory/', inventory_view, name='inventory'),
    path('edit_product/<int:pk>', edit_product, name='edit_product')"""
   
]