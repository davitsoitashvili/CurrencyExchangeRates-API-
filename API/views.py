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
    EUR = soup.find_all('tr')[7]

    USD_Rates = []
    EUR_Rates = []
    for usd_Item in USD:
        for usd_Rate in usd_Item:
            if usd_Rate.isdigit:
                USD_Rates.append(usd_Rate)

    for eur_item in EUR:
        for eur_Rate in eur_item:
            if eur_Rate.isdigit:
                EUR_Rates.append(eur_Rate)

    BuyUSD = USD_Rates[-2]
    SellUSD = USD_Rates[-4]

    BuyEUR = EUR_Rates[-2]
    SellEUR = EUR_Rates[-4]


    VTB_Rates = CurrencyRates(id = 1,bank_name="VTB Bank", buy_USD=BuyUSD, sell_USD=SellUSD, sell_EUR=SellEUR,buy_EUR=BuyEUR).save()


def TBC_Bank():
    url = requests.get('http://www.tbcbank.ge/web/en/exchange-rates')
    soup = BeautifulSoup(url.content, 'html.parser')
    rates = soup.find_all('div', class_='currRate')

    array_of_usd_rates = [usd.get_text()[8:] for usd in rates]
    array_of_eur_rates = [eur.get_text()[8:] for eur in rates]

    USD_Rates = [float(array_of_usd_rates[0]), float(array_of_usd_rates[1])]
    EUR_Rates = [float(array_of_eur_rates[2]), float(array_of_eur_rates[3])]

    BuyUSD = USD_Rates[1]
    SellUSD = USD_Rates[0]

    BuyEUR = EUR_Rates[1]
    SellEUR = EUR_Rates[0]

    TBC_Rates = CurrencyRates(id=2, bank_name="TBC Bank", buy_USD=BuyUSD, sell_USD=SellUSD,sell_EUR=SellEUR,buy_EUR=BuyEUR).save()


def Procredit_Bank():
    url = procredit_bank = requests.get('https://www.procreditbank.ge/en/exchange')
    soup_procredit_bank = BeautifulSoup(url.content, 'html.parser')

    BuyUSD = float(soup_procredit_bank.find_all('div', class_='exchange-sell')[0].get_text()[37:])
    SellUSD = float(soup_procredit_bank.find_all('div', class_='exchange-buy')[0].get_text()[37:])

    BuyEUR = float(soup_procredit_bank.find_all('div', class_='exchange-sell')[1].get_text()[37:])
    SellEUR = float(soup_procredit_bank.find_all('div', class_='exchange-buy')[1].get_text()[37:])

    Procredit_Rates = CurrencyRates(id=3, bank_name="Procredit Bank",buy_USD=BuyUSD,sell_USD=SellUSD,sell_EUR=SellEUR, buy_EUR=BuyEUR).save()


VTB_Bank()
TBC_Bank()
Procredit_Bank()



class CurrencyRatesList(APIView):

    def get(self, request):
        Rates = CurrencyRates.objects.all()
        Serializer = CurrencyRatesSerializer(Rates, many=True)
        return Response(Serializer.data)

    def post(self, request):
        pass