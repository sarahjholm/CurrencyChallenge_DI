from django.urls import path

from . import views

urlpatterns = [    
    path('<str:start_date>&<str:end_date>', views.get_currency_rate),
    path('<str:start_date>', views.get_currency_rate),
    path('', views.get_currency_rate)
]

