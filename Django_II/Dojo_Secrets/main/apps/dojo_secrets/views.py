from django.shortcuts import render, HttpResponse, redirect
from .models import User, Secret, UserManager
from django.contrib import messages
from django.db.models import Count
import bcrypt

def index(request):
    return render(request, 'dojo_secrets/index.html')

def login(request):
    if User.objects.filter(email = request.POST['email']):
        user = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            messages.error(request, "Successfully logged in!")
            return redirect('/profile')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect ('/')
    else:
        messages.error(request, "Invalid email or password.")
        return redirect('/')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed)
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name
        messages.error(request, "Successfully registered!")
        return redirect('/profile')

def profile(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view this page!")
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'first_name': request.session['first_name'],
        "Secrets": Secret.objects.annotate(count_likes=Count('liked_users')).order_by('-created_at'),
    }
  
    return render(request, 'dojo_secrets/profile.html', context)

def secret(request):
    secret = request.POST['secret']
    id = request.session['user_id']
    user = User.objects.get(id=id)
    Secret.objects.create(secret = secret, uploader = user)
    return redirect('/profile')

def popular(request):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view this page!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'first_name': request.session['first_name'],
        "Secrets": Secret.objects.annotate(count_likes=Count('liked_users')).order_by('-count_likes'),
    }
    return render(request, 'dojo_secrets/popular.html', context)

def like(request):
    if request.method == "POST":
        liked_users = Secret.objects.process_like(request.POST)
        return redirect('/profile')
        
def like_2(request):
    if request.method == "POST":
        liked_users = Secret.objects.process_like(request.POST)
    return redirect('/popular')

def logout(request):
    request.session.clear()
    return redirect('/')

def delete(request):
    this_secret = Secret.objects.get(id=request.POST['secret_id'])
    this_secret.delete()
    return redirect('/profile')

def delete_2(request):
    this_secret = Secret.objects.get(id=request.POST['secret_id'])
    this_secret.delete()
    return redirect('/popular') 