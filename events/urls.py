# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:38:59 2022

@author:  tanaka Maringire
"""

from django.urls import path 
from . import views

app_name = 'events'

urlpatterns = [path('', views.indexView, name= 'index' ),
               path('listings/', views.eventsView, name= 'listings'),
               path('listings/<int:Event_id>/', views.session, name ='session'),
               
               ]
