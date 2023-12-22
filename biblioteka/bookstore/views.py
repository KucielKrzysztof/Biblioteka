from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime


from django.views.decorators.csrf import ensure_csrf_cookie #upewnia się że jak wchodzisz pierwszy raz na te strone to pobierze ci token, tokeny są przechowywane w cookies a ktoś kto to odpala pierwszy raz w przeglądarce z jakiegoś powodu nie ma wygenerowanego tokenu więc nie ma go w cookies, nie ogarniam czemu
@ensure_csrf_cookie
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

def updateItem(request):
     data = json.loads(request.body) # Pobiera dane z ciała żądania
     productId = data['productId']
     action = data['action'] # Pobiera akcję (np. 'add' lub 'remove') z danych żądania
     #print('Action:', action)
     #print('ProductID:', productId)

     customer = request.user.customer
     product = Product.objects.get(id=productId)
     order, created = Order.objects.get_or_create(customer=customer, complete=False)  # Pobranie lub utworzenie elementu zamówienia dla określonego produktu i zamówienia
     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

     if action == 'add':
          orderItem.quantity = (orderItem.quantity + 1)
     elif action == 'remove':
          orderItem.quantity = (orderItem.quantity - 1)

     orderItem.save()  # Zapisanie zmian ilości produktu w elemencie zamówienia

     if orderItem.quantity <= 0:
          orderItem.delete()

     return JsonResponse('Item was added', safe=False)

def processOrder(request):
     #print('data:', request.body)
     data = json.loads(request.body)
     transaction_id = datetime.datetime.now().timestamp() #tworzy unikalny identyfikator transakcji na podstawie bieżącego znacznika czasowego. Ten identyfikator będzie unikalny, ponieważ znacznik czasowy jest unikalny w dowolnym momencie.

     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          order.transaction_id = transaction_id
          order.complete = True
          order.save()
     else:
          print('user is not logged in')

     return JsonResponse('order submitted', safe=False)
