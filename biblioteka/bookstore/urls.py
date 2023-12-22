from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name='update_item'),
    path('categorie_criminal/', views.categorieCriminal, name='categorie_criminal'),
    path('categorie_romance/', views.categorieRomance, name='categorie_romance'),
    path('categorie_fantasy/', views.categorieFantasy, name='categorie_fantasy'),
    path('categorie_scientific/', views.categorieScientific, name='categorie_scientific'),
    path('categorie_horror/', views.categorieHorror, name='categorie_horror'),
    

]