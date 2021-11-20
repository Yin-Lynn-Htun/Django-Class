from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Home page")

def daily(request, day):
    task_name = ''

    if day == 'monday':
        task_name = "Reveiw Python data types."
    elif day == 'tuesday':
        task_name = 'Review condition.'
    else:
        task_name = 'There is no tasks for this day.'

    return HttpResponse(task_name)