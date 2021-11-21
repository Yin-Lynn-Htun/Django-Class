from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

tasks = {
    'monday': "Reveiw Python data types.",
    'tuesday': "Review Condition.",
    'wednesday': 'learn django',
    'thursday': "Take a break",
    'friday': "Reveiw Python data types.",
    'saturday': "Review Condition.",
    'sunday': '',
}

def index(request):
    days = tasks.keys()
    return render(request, 'challenges/index.html' , {'days': days})


def daily(request, day): # monday - sunday
    try:
        task = tasks[day]
    except:
        return HttpResponseNotFound('Invalid day!')
    return render(request, 'challenges/daily_task.html', {'task': task, 'day': day})


def daily_by_number(request, day): # 1 - 7
    if day < 1 or day > 7:
        return HttpResponseNotFound('Invalid day!')

    days_list = list(tasks.keys())
    day= days_list[day-1]
    return HttpResponseRedirect(reverse('daily', args=(day,)) )

