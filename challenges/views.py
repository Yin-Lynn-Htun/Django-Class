from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tasks = {
    'monday': "Reveiw Python data types.",
    'tuesday': "Review Condition.",
    'wednesday': 'learn django',
    'thursday': "Take a break",
    'friday': "Reveiw Python data types.",
    'sat': "Review Condition.",
    'sun': 'learn django',
}

def index(request):
    return HttpResponse("Home page")


def daily(request, day):
    try:
        return HttpResponse(tasks[day])
    except:
        return HttpResponseNotFound('Invalid day!')