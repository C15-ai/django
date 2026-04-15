from django.urls import path
from .views import country_list, country_create , country_update , country_delete

urlpatterns = [
    path('country/list/', country_list, name='country_list'),
    path('country/create/', country_create, name='country_create'),
    path('country/update/<int:pk>/', country_update, name='country_update'),
    path('country/delete/<int:pk>/', country_delete, name='country_delete'),

]