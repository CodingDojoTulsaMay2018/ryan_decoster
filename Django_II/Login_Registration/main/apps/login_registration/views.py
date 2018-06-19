from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, UserManager

def index(request):
    return render(request, 'login_registration/index.html')

def register(request):
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['email'] = request.POST['email']

    errors = User.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed)
        return redirect('/success')

def login(request):
    if User.objects.filter(email = request.POST['email']):
        user = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            messages.error(request, "Successfully logged in!")
            return redirect('/success')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('/')
    else:
        messages.error(request, "Invalid email or password.")
        return redirect('/')


def success(request):
    context = {
        'name': request.session['first_name']
    }
    return render(request, 'login_registration/success.html', context)

def logout(request):
    request.session.clear()
    messages.error(request, "You have successfully logged out!")
    return redirect('/')