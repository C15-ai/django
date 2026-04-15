from django.urls import path


from .views import car_list, car_create, car_update, car_delete

urlpatterns = [
    path('car/list/', car_list, name='car_list'),
    path('car/create/', car_create, name='car_create'),
    path('car/update/<int:pk>/', car_update, name='car_update'),
    path('car/delete/<int:pk>/', car_delete, name='car_delete'),

]