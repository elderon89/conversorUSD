import json
from urllib.request import urlopen

with urlopen("http://www.apilayer.net/api/live?access_key=371a2caeeb86664b04e47d5777113568&format=1") as response:
    source = response.read()

usd_rates = dict()
for moedas, valores in json.loads(source)['quotes'].items():
    usd_rates[moedas] = valores

print(f"Convertendo 1 Dólar (USD) para Reais(BRL) => {usd_rates['USDBRL']}")
print(f"Convertendo 1 Dólar (USD) para EURO(EUR) => {usd_rates['USDEUR']}")
print(f"Convertendo 1 Dólar (USD) para Pesos Argentinos(ARS) => {usd_rates['USDARS']}")
print(f"Convertendo 1 Dólar (USD) para Dolar Australiano (AUD) => {usd_rates['USDAUD']}")
print(f"Convertendo 1 Dólar (USD) para Dolar Canadense (CAD) => {usd_rates['USDCAD']}")
print(f"Convertendo 1 Dólar (USD) para Peso Chileno (CLP) => {usd_rates['USDCLP']}")
