from django.shortcuts import render
from .models import *


def store(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) # Pobranie lub utworzenie niezakończonego zamówienia dla tego klienta
          items = order.orderitem_set.all() #Pobranie wszystkich elementów zamówienia (OrderItem) dla danego zamówienia (Order)
     else:
          items = []
          order = {'get_cart_items':0, }
     
     context = {'products':products, 'items': items, 'order':order} #Tworzy się słownik context, który zawiera dane, jakie zostaną przekazane do szablonu Django (store.html). Tutaj, 'products' jest kluczem w słowniku, a wartością jest lista produktów z bazy danych.
     return render(request, 'store/store.html', context)

def books(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) # Pobranie lub utworzenie niezakończonego zamówienia dla tego klienta
          items = order.orderitem_set.all() #Pobranie wszystkich elementów zamówienia (OrderItem) dla danego zamówienia (Order)
     else:
          items = []
          order = {'get_cart_items':0, }
     
     context = {'products':products, 'items': items, 'order':order} #Tworzy się słownik context, który zawiera dane, jakie zostaną przekazane do szablonu Django (store.html). Tutaj, 'products' jest kluczem w słowniku, a wartością jest lista produktów z bazy danych.
     return render(request, 'store/books.html', context)

def cart(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) # Pobranie lub utworzenie niezakończonego zamówienia dla tego klienta
          items = order.orderitem_set.all() #Pobranie wszystkich elementów zamówienia (OrderItem) dla danego zamówienia (Order)
     else:
          items = []
          order = {'get_cart_items':0, }
     context = {'items': items, 'order':order}
     return render(request, 'store/cart.html', context)

def checkout(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) # Pobranie lub utworzenie niezakończonego zamówienia dla tego klienta
          items = order.orderitem_set.all() #Pobranie wszystkich elementów zamówienia (OrderItem) dla danego zamówienia (Order)
     else:
          items = []
          order = {'get_cart_items':0, }
     context = {'items': items, 'order':order}
     return render(request, 'store/checkout.html', context)

