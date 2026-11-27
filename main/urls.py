from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('inventory/', views.inventory_list, name='inventory'),

    path('inventory/add/', views.add_card, name='add_card'),

    path('inventory/edit/<int:card_id>/', views.edit_card, name='edit_card'),

    path('inventory/delete/<int:card_id>/', views.delete_card, name='delete_card'),
]