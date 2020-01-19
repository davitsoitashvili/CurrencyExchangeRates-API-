from django.shortcuts import render
from API.models import CurrencyRates,BankNames
from API.serializers import CurrencyRatesSerializer,BankNamesSerializer
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

    BankNames(id=1,bank_name="VTB Bank", image_url="https://is1-ssl.mzstatic.com/image/thumb/Purple113/v4/2c/77/9c/2c779c5a-6cd2-e6fb-296f-5afdc57fd761/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-85-220.png/246x0w.png").save()
    CurrencyRates(id = 1,buy_USD=BuyUSD, sell_USD=SellUSD, sell_EUR=SellEUR,buy_EUR=BuyEUR).save()


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

    BankNames(id=2,bank_name="TBC Bank", image_url="https://bm.ge/uploads/news/5b3cbcb38b54e.png").save()
    CurrencyRates(id=2, buy_USD=BuyUSD, sell_USD=SellUSD,sell_EUR=SellEUR,buy_EUR=BuyEUR).save()


def Procredit_Bank():
    url = procredit_bank = requests.get('https://www.procreditbank.ge/en/exchange')
    soup_procredit_bank = BeautifulSoup(url.content, 'html.parser')

    BuyUSD = float(soup_procredit_bank.find_all('div', class_='exchange-sell')[0].get_text()[37:])
    SellUSD = float(soup_procredit_bank.find_all('div', class_='exchange-buy')[0].get_text()[37:])

    BuyEUR = float(soup_procredit_bank.find_all('div', class_='exchange-sell')[1].get_text()[37:])
    SellEUR = float(soup_procredit_bank.find_all('div', class_='exchange-buy')[1].get_text()[37:])

    BankNames(id=3,bank_name="Procredit Bank", image_url="https://innobyte.com/wp-content/uploads/2013/03/procreditbank-thumbnail.jpg").save()
    CurrencyRates(id=3,buy_USD=BuyUSD,sell_USD=SellUSD,sell_EUR=SellEUR, buy_EUR=BuyEUR).save()


def Georgian_Bank():
    url = requests.get("https://bankofgeorgia.ge/wealth/en/Treasury-operations/exchange-rates")
    soup = BeautifulSoup(url.content, "html.parser")
    BuyUSD = soup.find_all("td")[9].text.strip()
    SellUSD = soup.find_all("td")[8].text.strip()
    BuyEUR = soup.find_all("td")[14].text.strip()
    SellEUR = soup.find_all("td")[13].text.strip()

    BankNames(id=4,bank_name="Bank of Georgia", image_url="https://bm.ge/uploads/news/5b053053866f0.png").save()
    CurrencyRates(id=4, buy_USD=BuyUSD, sell_USD=SellUSD,buy_EUR=BuyEUR,sell_EUR=SellEUR).save()

VTB_Bank()
TBC_Bank()
Procredit_Bank()
Georgian_Bank()


class CurrencyRatesList(APIView):
    def get(self, request,id=None):
        if id == None:
            Rates = CurrencyRates.objects.all()
            Serializer = CurrencyRatesSerializer(Rates, many=True)
            return Response(Serializer.data)
        else:
            Rate = CurrencyRates.objects.get(id=id)
            Serializer = CurrencyRatesSerializer(Rate)
            return Response(Serializer.data)

    def post(self, request):
        pass

class BankNamesList(APIView):
    def get(self,request,id=None):
        if id==None:
            Names = BankNames.objects.all()
            NamesSerializer = BankNamesSerializer(Names,many=True)
            return Response(NamesSerializer.data)
        else:
            Names = BankNames.objects.get(id=id)
            NamesSerializer = BankNamesSerializer(Names)
            return Response(NamesSerializer.data)

    def post(self, request):
        pass