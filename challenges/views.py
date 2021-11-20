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
    'saturday': "Review Condition.",
    'sunday': 'learn django',
}

def index(request):
    return HttpResponse("Home page")


def daily(request, day):
    try:
        return HttpResponse(tasks[day])
    except:
        return HttpResponseNotFound('Invalid day!')


def daily_by_number(request, day): # 1 - 7
    if day < 1 or day > 7:
        return HttpResponseNotFound('Invalid day!')

    task_list = list(tasks.values())
    task = task_list[day-1]
    return HttpResponse(task)