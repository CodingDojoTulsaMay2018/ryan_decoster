from django.shortcuts import render, HttpResponse, redirect

def index(request):
    
    return render(request, "surveys/index.html")

def submit(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']  
    return redirect('/result')


def result(request):
    context = {
        'counter': request.session['counter'],
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
    }
    return render(request, "surveys/results.html", context)

