from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager, Message, Comment
import bcrypt

def index(request):

    return render(request, ('dashboard/index.html'))

def login(request):
    
    return render(request, ('dashboard/login.html'))

def loginCheck(request):
    if User.objects.filter(email = request.POST['email']):
        user = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            print(request.session['user_id'])
            if user.user_level==True:            
                messages.error(request, "Successfully logged in!")
                return redirect('dashboard/admin')
            else:
                messages.error(request, "Successfully logged in!")
                return redirect('/dashboard')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('/login')
    else:
        messages.error(request, "Invalid email or password.")
        return redirect('/login')



def register(request):
    
    return render(request, 'dashboard/register.html')

def create(request):
    request.session['first_name'] = request.POST['first_name']

    errors = User.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed)
        request.session['user_id'] = user.id
        messages.error(request, "Successfully registered!")
        return redirect('/dashboard')
    return redirect('/register')

def createNew(request):
    request.session['first_name'] = request.POST['first_name']

    errors = User.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed)
        request.session['user_id'] = user.id
        messages.error(request, "Successfully created a new user!")
        return redirect('/dashboard/admin')
    return redirect('/users/new')

def dashboard(request):
    print(request.session['user_id'])
    context = {
        'Users': User.objects.all(),  
    }
    return render(request, 'dashboard/dashboard.html', context)

def admin(request):
    context = {
        'Users': User.objects.all()
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

def new(request):

    return render(request, 'dashboard/new.html')

def adminEdit(request, id):
    context = {
        'id': id,
        'first_name': User.objects.get(id=id).first_name,
        'last_name': User.objects.get(id=id).last_name,
        'email': User.objects.get(id=id).email,
        'user_level': User.objects.get(id=id).user_level
    }

    return render(request, 'dashboard/adminEdit.html', context)

def edit(request, id):
    
    context = {
        'id': request.session['user_id'],
        'first_name': User.objects.get(id=id).first_name,
        'last_name': User.objects.get(id=id).last_name,
        'email': User.objects.get(id=id).email,
    }
    return render(request, 'dashboard/edit.html', context)

def updateInfo(request, id):
    user = User.objects.get(id=id)
    errors = User.objects.infoValidator(request.POST)
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
        return redirect('/dashboard')

def adminUpdateInfo(request, id):
    user = User.objects.get(id=id)
    errors = User.objects.adminInfoValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/'+str(user.id)+'/adminEdit')
    else:
        user = User.objects.get(id=id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.user_level = request.POST['user_level']
        user.save()
        return redirect('/dashboard/admin')

def updatePassword(request, id):
    user = User.objects.get(id=id)
    errors = User.objects.passwordValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/'+str(user.id)+'/edit')
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.get(id=id)
        user.password = hashed
        user.save()
        messages.error(request, "Password updated successfully!")
        return redirect('/dashboard')

def updateDescription(request, id):
    user = User.objects.get(id=id)
    user.description = request.POST['desc_area']
    user.save()
    messages.error(request, "Description updated successfully!")
    return redirect('/dashboard')

def adminUpdatePassword(request, id):
    user = User.objects.get(id=id)
    errors = User.objects.passwordValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/'+str(user.id)+'/adminEdit')
    else:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.get(id=id)
        user.password = hashed
        user.save()
        messages.error(request, "Password updated successfully!")
        return redirect('/dashboard/admin')

def show(request, id):
    context = {
        'id': id,
        'first_name': User.objects.get(id=id).first_name,
        'last_name': User.objects.get(id=id).last_name,
        'email': User.objects.get(id=id).email,
        'created_at': User.objects.get(id=id).created_at,
        'desc': User.objects.get(id=id).desc,
        'Users': User.objects.all(),
        'Messages': Message.objects.all(),
        'Comments': Comment.objects.all(),
    }
    return render(request, 'dashboard/show.html', context)

def message(request, id):
    id = request.session['user_id']
    user = User.objects.get(id=id)
    Message.objects.create(message = request.POST['message'], user=user)

    return redirect('/users/'+str(user.id)+'/show')

def comment(request, id):
    id = request.session['user_id']
    user = User.objects.get(id=id)
    message_id = request.POST['message_id']
    comment = request.POST['comment']
    
    Comment.objects.create(comment = comment, user_id = user, message_id = message_id)

    return redirect('/users/'+str(user.id)+'/show')

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/dashboard/admin')

def logout(request):
    request.session.clear()
    messages.error(request, "Successfully logged out!")
    return redirect('/')

