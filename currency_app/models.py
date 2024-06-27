from django.db import models

class CurrencyRate(models.Model) :
    date = models.DateTimeField(unique=True)
    value = models.FloatField(max_length=6)

"""
class RequestedRates(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    value = models.FloatField(max_length=6)
"""
