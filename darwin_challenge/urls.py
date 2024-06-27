from django.urls import include, path

urlpatterns = [
    path('currencyapi/', include("currency_app.urls"))
]
