from django.shortcuts import render, HttpResponse, redirect
import random
from time import localtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    context = {
        'gold': request.session['gold']
    }
    return render(request, "ninjagold/index.html", context)

def process(request):
    if 'farm' in request.POST['building']:
        collected = random.randrange(10, 20)
        request.session['gold'] += collected
        request.session['activities'].append({'color': 'green', 'location' : 'farm', 'gold' : collected, 'time': strftime("%Y/%m/%d %I:%M %p", localtime()) })
    if 'cave' in request.POST['building']:
        collected = random.randrange(5, 10)
        request.session['gold'] += collected
        request.session['activities'].append({'color': 'green', 'location' : 'cave', 'gold' : collected, 'time': strftime("%Y/%m/%d %I:%M %p", localtime()) })
    if 'house' in request.POST['building']:
        collected = random.randrange(2, 5)
        request.session['gold'] += collected
        request.session['activities'].append({'color': 'green', 'location' : 'house', 'gold' : collected, 'time': strftime("%Y/%m/%d %I:%M %p", localtime()) })
    if 'casino' in request.POST['building']:
        if request.session['gold'] <= 0:
            request.session['activities'].append("You can't gamble with nothing!")
        else:
            collected = random.randrange(-50, 50) 
            request.session['gold'] += collected
            if collected > 0:
                request.session['activities'].append({'color': 'green', 'location' : 'casino', 'gold' : collected, 'time': strftime("%Y/%m/%d %I:%M %p", localtime()) })
            else:
                request.session['activities'].append({'color': 'red', 'location' : 'casino', 'gold' : collected, 'time': strftime("%Y/%m/%d %I:%M %p", localtime()) })
        if request.session['gold'] <= 0:
            request.session['gold'] = 0
    
    return redirect('/')
