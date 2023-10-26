#เลขาของ myapp

from django.urls import path
from .views import Homepage, About, Service, Products , Contact


urlpatterns = [
    path('',  Homepage, name='home'), # localhost:8000
    path('about', About, name='about'),
    path('service', Service, name='service'),
    path('products', Products, name='products'),
    path('contact', Contact, name='contact'),
]