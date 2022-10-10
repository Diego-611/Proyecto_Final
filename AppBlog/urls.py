from django.urls import path
from .views import *



urlpatterns = [
    path('', viewIndex, name='Home'),
    path('home/',viewRIndex, name='RHome'),
    path('page/<id>', viewBlog, name='Blog'),
    path('about/', viewAbout, name='About')
]