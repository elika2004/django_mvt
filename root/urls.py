from django.urls import path
from .views import home , contact , about ,agents

app_name='root'

urlpatterns=[
    path('',home,name='home'),
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('agents',agents,name='agents'),
    
]
