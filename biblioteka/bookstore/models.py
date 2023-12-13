from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    isTeacher = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    #image - do dodania
    #czy jest nie fizyczny
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model): #koszyk
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    data_ordered = models.DateTimeField(auto_now_add=True) #bieżąca data i godzina
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=40, null=True)

    def __str__(self):
        return str(self.id) #id to autogenerowany primary key obiektu Order

class OrderItem(models.Model): #produkt w koszyku
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)