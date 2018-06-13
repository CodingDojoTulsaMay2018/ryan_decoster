from django.shortcuts import render, HttpResponse
from time import localtime, strftime

def index(request):
    context = {
        "day": strftime("%b %d, %Y", localtime()),
        "time": strftime("%I:%M %p", localtime())
    }
    return render(request, 'time_display/index.html', context)

