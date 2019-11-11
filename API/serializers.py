from rest_framework import serializers
from API.models import CurrencyRates
class CurrencyRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRates
        fields = ["bank_name", "sell_USD", "buy_USD", "sell_EUR", "buy_EUR"]
