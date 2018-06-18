from django.shortcuts import render, redirect
from .models import Item

def index(request):
    context = {
        'Items': Item.objects.all()
    }
    return render(request, 'amadon/index.html', context)

def buy(request):
    request.session['quantity'] = request.POST['quantity']
    request.session['id'] = request.POST['id']
    id = int(request.session['id'])

    quantity = float(request.session['quantity'])
    price = float(Item.objects.get(id=id).price)
    request.session['total'] = quantity * price

    if 'counter' not in request.session:
        request.session['counter'] = int(quantity)
    request.session['counter'] += int(quantity)
    
    if 'sum' not in request.session:
        request.session['sum'] = request.session['total']
    request.session['sum'] += request.session['total']

    return redirect('/checkout')

def checkout(request):
    id = int(request.session['id'])
    context = {
        'id': id,
        'name': Item.objects.get(id=id).name,
        'total': request.session['total'],
        'counter': request.session['counter'],
        'sum': request.session['sum']
    }
    return render(request, 'amadon/checkout.html', context)