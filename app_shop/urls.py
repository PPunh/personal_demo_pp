from django.urls import path
from . import views

urlpatterns = [
    path('', views.allProducts, name='shop'),
    path('dashboard_admin/', views.custom_dashboard_admin, name='dashboard_admin'),
    path('add_product/', views.add_product, name='add_product'),
]