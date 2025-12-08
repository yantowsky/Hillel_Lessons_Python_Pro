from django.urls import path
from .views import member_list, create_member

urlpatterns = [
    path('', member_list, name='member_list'),
    path('create/', create_member, name='create_member'),
]
