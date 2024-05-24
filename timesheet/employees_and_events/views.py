from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from employees_and_events.models import *


def person_view(request, person_id):
    
    
    try:
        person = Person.objects.get(pk=person_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    
    return render(request, "person_view.html", {"person": person})
 #    
#     html = f"<html><body>Person name is {person.first_name} {person.surname}</body></html>"
#     return HttpResponse(html)


def people_view(request):
    try:
        people = Person.objects.all()
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    
    return render(request, "people_view.html", {"people": people})