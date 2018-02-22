'''
Created on 22 Feb 2018

@author: anthony white
'''

from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    ]

