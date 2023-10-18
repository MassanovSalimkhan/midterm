from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/', '<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('contacts/add/', views.add.contact),
]
