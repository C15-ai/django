from django.urls import path
from .views import  *

urlpatterns = [
    path('club/list/', club_list, name='club_list'),
    path('club/detail/<int:pk>/', club_detail, name='club_detail'),
    # path('create-form/', club_create_form, name='book_create_form'),
    path('club/create/', club_create, name='club_create'),
    path('club/update/<int:pk>/', club_update, name='club_update'),
    # path('update-form/<int:pk>/', club_update_form, name='book_update_form'),
    path('club/delete/<int:pk>/', club_delete, name='club_delete'),

]



