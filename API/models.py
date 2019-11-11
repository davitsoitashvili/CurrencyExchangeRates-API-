from django.db import models

class CurrencyRates(models.Model):
    bank_name = models.CharField(max_length=100)
    sell_USD = models.FloatField()
    buy_USD = models.FloatField()
    sell_EUR = models.FloatField()
    buy_EUR = models.FloatField()
