from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_list, name='order_list'),
    path('order_create/', views.order_create, name='order_create'),

]