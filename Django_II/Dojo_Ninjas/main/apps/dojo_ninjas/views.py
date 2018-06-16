from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        'Dojos': Dojo.objects.all()
}
    return render(request, "dojo_ninjas/index.html", context)