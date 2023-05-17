from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.product_detail, name='detail'),
    path('', views.productos, name='productos'),
    path('busqueda', views.buscar_productos, name='busqueda')
]