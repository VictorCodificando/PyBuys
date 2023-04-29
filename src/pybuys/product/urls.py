from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('new/', views.product_new, name='product_new'),
    path('edit/<int:pk>/', views.product_edit, name='product_edit'),    
    path('buy/<int:pk>/', views.product_delete, name='product_buy'),
]