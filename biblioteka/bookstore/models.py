from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    isTeacher = models.BooleanField(default=False) #bo nauczyciele mają potem mieć, że nielimitowany czas wypozyczenia

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)  #czy jest nie fizyczny
    genre = models.CharField(max_length=100, null=True) #gatunek ksiązki
    author = models.CharField(max_length=100, null=True)
    #description
    id = models.AutoField(primary_key=True, editable=False) #autonumerowane pole jako pk
    isbn = models.CharField(max_length=17, unique=True, null=True) #ISBN
    #link dal pdf-ów
    image = models.ImageField(null=True, blank=True)

    @property #dekorator pozwalający dotrzeć do tego jako atrybut a nie metoda
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

    def __str__(self):
        return self.name


class Order(models.Model): #koszyk
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    data_ordered = models.DateTimeField(auto_now_add=True) #bieżąca data i godzina
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=40, null=True)
    #status = models.CharField(max_length=20, choices=[('wypożyczona', 'Wypożyczona'), ('zwrócona', 'Zwrócona')])

    def __str__(self):
        return str(self.id) #id to autogenerowany primary key obiektu Order
    
    @property
    def get_cart_items(self): #zlicza ile produktów ejst w koszyku
        
        order_items = self.orderitem_set.all()  # Pobierz wszystkie elementy OrderItem dla tego zamówienia
        total_items = 0

        # Zlicz wszystkie produkty sumując ich ilość
        for item in order_items:
            total_items += item.quantity

        return total_items

class OrderItem(models.Model): #produkt w koszyku
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)