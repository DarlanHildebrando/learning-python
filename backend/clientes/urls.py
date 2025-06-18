from django.urls import path
from .views import ClientView

urlPatterns = [
    
    path('clientes/', ClientView.as_view())

]