from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    context = {
        "generate": get_random_string(length=14)
    }
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:  
        request.session['counter'] += 1
    
    return render(request, 'random_word/index.html', context)
print('I am above reset')
def reset(request):
    request.session.clear()

    return redirect('/random_word')
