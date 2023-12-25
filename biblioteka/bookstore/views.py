from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required #importuje dekorator który sprawdza czy user jest zalogowany, jeśli nie to przekierowuje na stronę logowania
from django.contrib.auth.views import LoginView #wbudowany login view w django
from django.contrib.auth import authenticate, login, logout #wbudowane funkcje do logowania
from datetime import timedelta #do obliczania daty zwrotu
from django.db.models import Q #do tworzenia zapytań z wieloma warunkami


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

@login_required
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


@login_required#w setting.py  ustaw: LOGIN_URL = '/login/' - login = nazwa urla albo url
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



@login_required #w setting.py  ustaw: LOGIN_URL = '/login/' - login = nazwa urla albo url
def profile(request):
     customer = request.user.customer
     order, created = Order.objects.get_or_create(customer=customer, complete=False) # Pobranie lub utworzenie niezakończonego zamówienia dla tego klienta
     items = order.orderitem_set.all() #Pobranie wszystkich elementów zamówienia (OrderItem) dla danego zamówienia (Order)
     orders = Order.objects.filter(customer=customer, complete=True)
     
     context = {'orders': orders,'customer':customer,'items': items, 'order':order}
     return render(request, 'store/profile.html', context)

#nasz login view
def myLogin(request):
     if request.user.is_authenticated: #jeśli zalogowany użytkownik próbuje wejść na stronę logowania to przekierowuje go na stronę główną
        return redirect('store')

     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('store')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Niepoprawne dane logowania')
            return render(request, 'registration/login.html', {'messages': messages.get_messages(request),'is_login_page': True})
     else:
        return render(request, 'registration/login.html', {'is_login_page': True})

#logout view:
def myLogout(request):
    logout(request)
    return redirect('store') 
#####


###viewsy do stron z książkami
def books(request):
     query = request.GET.get('q') #pobiera do widoku parametr q  który przechowuje wartość wprowadzoną przez użytkownika do naszego search bara
     products = Product.objects.all()
     if query:  # If a query parameter is present
        products = products.filter(Q(name__icontains=query) | Q(author__icontains=query))  # filtruje produkty po nazwie lub autorze
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) 
          items = order.orderitem_set.all() 
     else:
          items = []
          order = {'get_cart_items':0, }

     context = {'products':products, 'items': items, 'order':order} 
     return render(request, 'store/books.html', context)

def digitals(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) 
          items = order.orderitem_set.all() 
     else:
          items = []
          order = {'get_cart_items':0, }

     context = {'products':products, 'items': items, 'order':order}
     return render(request, 'store/digitals.html', context)

def details(request, product_id):
     book = get_object_or_404(Product, pk=product_id)
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()
     else:
          items = []
          order = {'get_cart_items': 0}

     context = {'book': book, 'items': items, 'order': order}
     return render(request, 'store/details.html', context)

def categorieCriminal(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) 
          items = order.orderitem_set.all() 
     else:
          items = []
          order = {'get_cart_items':0, }
     
     context = {'products':products, 'items': items, 'order':order} 
     return render(request,'store/categorieCriminal.html',context)

def categorieRomance(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) 
          items = order.orderitem_set.all() 
     else:
          items = []
          order = {'get_cart_items':0, }
     
     context = {'products':products, 'items': items, 'order':order} 
     return render(request,'store/categorieRomance.html',context)

def categorieScientific(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) 
          items = order.orderitem_set.all() 
     else:
          items = []
          order = {'get_cart_items':0, }
     
     context = {'products':products, 'items': items, 'order':order} 
     return render(request,'store/categorieScientific.html',context)

def categorieHorror(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) 
          items = order.orderitem_set.all() 
     else:
          items = []
          order = {'get_cart_items':0, }
     
     context = {'products':products, 'items': items, 'order':order} 
     return render(request,'store/categorieHorror.html',context)

def categorieFantasy(request):
     products = Product.objects.all()
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False) 
          items = order.orderitem_set.all() 
     else:
          items = []
          order = {'get_cart_items':0, }
     
     context = {'products':products, 'items': items, 'order':order} 
     return render(request,'store/categorieFantasy.html',context)


###functions to handle AJAX requests:
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
     #data = json.loads(request.body)
     transaction_id = datetime.datetime.now().timestamp() #tworzy unikalny identyfikator transakcji na podstawie bieżącego znacznika czasowego. Ten identyfikator będzie unikalny, ponieważ znacznik czasowy jest unikalny w dowolnym momencie.

     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          order.transaction_id = transaction_id
          order.complete = True
          order.data_ordered = datetime.datetime.now()
          response ={}
          if customer.isTeacher==False:
               order.return_data = datetime.datetime.now() + timedelta(days=7)# + timedelta(days=7) #dodaje 30 dni do daty zwrotu
               response = {'transaction_id': transaction_id,
                           }
          elif customer.isTeacher==True:
               response = {'transaction_id': transaction_id,
                           }
          order.save()
     else:
          print('user is not logged in')

     return JsonResponse(response, safe=False)
