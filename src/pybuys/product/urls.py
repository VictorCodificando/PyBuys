from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.product_detail, name='detail'),
    path('new/', views.product_new, name='new'),
    path('edit/<int:pk>/', views.product_edit, name='edit'),
    path('', views.productos, name='productos'),
]