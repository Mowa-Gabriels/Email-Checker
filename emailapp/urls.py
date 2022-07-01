
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.email_list, name='email_list'),
    path('add/', views.email_add, name='add_email')
]
