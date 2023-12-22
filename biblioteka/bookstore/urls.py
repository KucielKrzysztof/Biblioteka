from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('books/', views.books, name="books"),
    path('digitals/', views.digitals, name="digitals"),
    path('details/<int:product_id>/', views.details, name="details"),

]