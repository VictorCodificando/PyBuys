from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('add_to_cart/<int:id_producto>/', views.add_to_cart, name='add_to_cart'),
    path('buy/', views.buy, name='buy'),
]