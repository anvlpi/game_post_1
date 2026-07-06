from django.urls import path
from . import views


app_name = 'other_pages'
urlpatterns = [
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
]
