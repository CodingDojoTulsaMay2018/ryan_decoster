from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course

def index(request):
    context = {
        'Courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
        return redirect('/')

def destroy(request, id):
    context = {
        'id': id,
        'name': Course.objects.get(id=id).name,
        'desc': Course.objects.get(id=id).desc
    }
    return render(request, 'courses/remove.html', context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')