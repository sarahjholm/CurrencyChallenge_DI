from django.db import models

class CurrencyRate(models.Model) :
    date = models.DateTimeField(unique=True)
    value = models.FloatField(max_length=6)
