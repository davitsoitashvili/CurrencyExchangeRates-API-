from django.db import models

class CurrencyRates(models.Model):
    sell_USD = models.FloatField()
    buy_USD = models.FloatField()
    sell_EUR = models.FloatField()
    buy_EUR = models.FloatField()

class BankNames(models.Model):
    bank_name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)

    def __str__(self):
        return self.bank_name
