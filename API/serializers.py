from rest_framework import serializers
from API.models import CurrencyRates,BankNames
class CurrencyRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRates
        fields = ["sell_USD", "buy_USD", "sell_EUR", "buy_EUR"]


class BankNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankNames
        fields = ["bank_name", "image_url"]
