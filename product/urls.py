from django.urls import path
from .views import product_list, product_create, product_update

urlpatterns = [
    path('product/list/', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/update/<int:pk>/', product_update, name='product_update'),

]

