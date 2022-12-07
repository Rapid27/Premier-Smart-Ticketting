from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Event
from django.views.generic.base import View
from django.urls import reverse
import pandas as pd
import numpy as np


# Create your views here.

def indexView(request):
    
    return render(request, 'events/index.html')

def eventsView(request):
    
    latest_events_list = Event.objects.order_by('-Date_created')[:5]
    
    context = {'latest_events_list': latest_events_list,
        }
    
    
    return render(request, 'events/listings.html' , context)

#class Session(View):
    
 #   data = np.ndarray()
    
  #  def loaddata( self, Event):

def session(request, Event_id):
    
    selected_event = get_object_or_404(Event, pk= Event_id)
    
    event_data = selected_event.load_data()
    
    attendees = selected_event.attendance
    
    
        
    
    try: 
            scanned_member = [request.POST['CheckIn']]
        
    except (KeyError):
            
            return render(request, 'events/session.html', {'selected_event': selected_event,
                                                           'event_data': event_data,
                                                           'error_message': " You did not submit anything",
                })
        
    else:
        
        if( scanned_member in event_data and scanned_member not in attendees ):
            
            success_message = "Ticket valid!!!"
            
            attendees.append(scanned_member)
            
            selected_event.save()
            
            return render(request, 'events/session.html', {'selected_event': selected_event,
                                                           'event_data': event_data,
                                                           'success_message': success_message,
                                                           })
        
        if( scanned_member in event_data and scanned_member in attendees):
            
            failure_message = "Ticket is already checked in !!!"
            
            return render(request, 'events/session.html', {'selected_event': selected_event,
                                                           'event_data': event_data,
                                                           'failure_message': failure_message,
                                                           })
        
        if(scanned_member not in event_data):
            
            null_message = "Ticket not in database!!!"
            
            return render(request, 'events/session.html', {'selected_event': selected_event,
                                                           'event_data': event_data,
                                                           'null_message': null_message,
                                                           })
            
            
            
            
            
            
            
            
            
            
            
    
    
# c
# def js read csv files 
    
    
    
        
    