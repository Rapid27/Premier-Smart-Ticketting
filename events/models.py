from django.db import models
from django.utils import timezone
import pandas as pd
import numpy as np

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length= 100,
                            unique= True,
            error_messages= {'unique':'A client with this title already exists'}
                            )
    
    Contact_details = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    

class Event(models.Model):
    
    title = models.CharField(
        max_length=200 ,
        unique = False,
        
        )
    
    Date_created = models.DateTimeField(auto_now_add= True)
    Event_Date = models.DateTimeField('Event Date')
    
    Event_Location = models.CharField(
        max_length= 100,
        )
    
    Hosting_Client = models.ForeignKey( Client,
                                       blank = True,
                                       null = True,
                                       on_delete= models.CASCADE
                                       )
    Event_Data = models.FileField(upload_to='csv')
    
    #converting the csv file data to a python list
    def load_data(self):
        event_list = pd.read_csv(self.Event_Data).to_numpy().tolist()
        
        return event_list
    
    #creating a list for attendance recording
    
    attendance = []
    
        

    
    def __str__(self):
        return self.title
    

    
class After_Event_Summary(models.Model):
    
    Event_Notes = models.TextField()
    event = models.ForeignKey(Event,
                              on_delete= models.CASCADE)

    
    def __str__(self):
        return self.Event_Notes
    
    