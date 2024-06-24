from django.db import models

class CurrencyRate(models.Model) :
    date = models.DateTimeField()
    value = models.FloatField(max_length=6)
