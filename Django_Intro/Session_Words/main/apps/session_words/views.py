from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    if 'list' not in request.session:
        request.session['list'] = []
    
    context = {
        'list': request.session['list'] 
    }
    return render(request, "session_words/index.html", context)

def submit(request):
    request.session['word'] = request.POST['word']

    request.session['time'] = strftime("%b %d, %Y %I:%M %p", localtime())

    if 'font' not in request.POST:
        request.session['font'] = '16px'
    else:
        request.session['font'] = '40px'

    if 'color' not in request.POST:
        request.session['color'] = 'black'
    else:
        request.session['color'] = request.POST['color']

    temp_list = request.session['list']
    temp_list.append({'word': request.session['word'], 'color': request.session['color'], 'font': request.session['font'], 'time': '- added on ' + request.session['time']})
    request.session['list'] = temp_list

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')