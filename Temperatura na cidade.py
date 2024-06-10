# pip install beautifulsoup4
# pip install requests

from bs4 import BeautifulSoup
import requests

# Pesquise a cidade no endereço https://www.climatempo.com.br/previsao-do-tempo
# Copie o endereço URL da página da cidade e cole entre os apóstrofos (ou aspas) da linha abaixo
URL_da_cidade = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/353/caxiasdosul-rs'
html = requests.get(URL_da_cidade).content

soup = BeautifulSoup(html, 'html.parser')

tempMin = soup.find(id='min-temp-1')
tempMax = soup.find(id='max-temp-1')

print('Temp. Minima: ' + tempMin.string)
print('Temp. Maxima: ' + tempMax.string)

input('\nAperte ENTER para sair...')