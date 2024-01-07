from django.urls import path
from .views import index,templateexample

urlpatterns =[
    path('home/',index,name='home'),
    path('template/',templateexample, name = 'template')
]

