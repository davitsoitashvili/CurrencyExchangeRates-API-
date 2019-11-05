from django.shortcuts import render
from API.models import CurrencyRates
from API.serializers import CurrencyRatesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from bs4 import BeautifulSoup

def VTB_Bank():
    url = requests.get("https://vtb.ge/en/individuals/exchange-rates")
    soup = BeautifulSoup(url.content, "html.parser")
    USD = soup.find_all("tr")[1]
    info = {}
    Price_result = []
    for item in USD:
        for result in item:
            if result.isdigit:
                Price_result.append(result)

    BuyUSD = Price_result[-2]
    SellUSD = Price_result[-4]

    VTB_Rates = CurrencyRates(id = 1,bank_name="VTB Bank", buy_USD=BuyUSD, sell_USD=SellUSD).save()


def TBC_Bank():
    url = requests.get('http://www.tbcbank.ge/web/en/exchange-rates')
    soup = BeautifulSoup(url.content, 'html.parser')
    valute = soup.find_all('div', class_='currRate')

    info = {}
    array_of_valute = [price.get_text()[8:] for price in valute]
    USD_GEL = [float(array_of_valute[0]), float(array_of_valute[1])]

    BuyUSD = USD_GEL[1]
    SellUSD = USD_GEL[0]

    TBC_Rates = CurrencyRates(id=2, bank_name="TBC Bank", buy_USD=BuyUSD, sell_USD=SellUSD).save()


def Procredit_Bank():
    url = procredit_bank = requests.get('https://www.procreditbank.ge/en/exchange')
    soup_procredit_bank = BeautifulSoup(url.content, 'html.parser')

    BuyUSD = float(soup_procredit_bank.find_all('div', class_='exchange-sell')[0].get_text()[37:])
    SellUSD = float(soup_procredit_bank.find_all('div', class_='exchange-buy')[0].get_text()[37:])

    Procredit_Rates = CurrencyRates(id=3, bank_name="Procredit Bank",buy_USD=BuyUSD,sell_USD=SellUSD).save()


 

class CurrencyRatesList(APIView):

    def get(self, request):
        Rates = CurrencyRates.objects.all()
        Serializer = CurrencyRatesSerializer(Rates, many=True)
        return Response(Serializer.data)

    def post(self, request):
        pass