from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name='update_item'),
	path('process_order/', views.processOrder, name='process_order'),
	path('profile', views.profile, name='profile'),
    path('login/', views.myLogin, name='login'),
    path('logout/', views.myLogout, name='logout'),
    
]