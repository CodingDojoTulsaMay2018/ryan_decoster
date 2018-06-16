from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, UserManager

def index(request):
    for object in User.objects.all():
        context = {
            'id': object.id,
            'first_name': object.first_name,
            'last_name': object.last_name,
            'email': object.email,
            'created_at':object.created_at
        }

    context = {
        'Users': User.objects.all()
    }
    return render(request, "users/index.html", context)

def new(request):
    return render(request, 'users/create.html')

def create(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')
    else:
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        return redirect('/users/'+str(user.id))

def show(request, id):
    context = {
        'id': id,
        'first_name': User.objects.get(id=id).first_name,
        'last_name': User.objects.get(id=id).last_name,
        'email': User.objects.get(id=id).email,
        'created_at': User.objects.get(id=id).created_at
    }
    return render(request, 'users/show.html', context)

def edit(request, id):
    context = {
        'id': id,
        'first_name': User.objects.get(id=id).first_name,
        'last_name': User.objects.get(id=id).last_name,
        'email': User.objects.get(id=id).email,
    }
    return render(request, 'users/edit.html', context)


def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')

def update(request, id):
    user = User.objects.get(id=id)
    errors = User.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/'+str(user.id)+'/edit')
    else:
        user = User.objects.get(id=id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users')
    
