from django.contrib import admin
from .models import Event,Client,After_Event_Summary

# Register your models here.

model_list = [Event, Client, After_Event_Summary]
admin.site.register(model_list)
