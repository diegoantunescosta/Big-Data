from bs4 import BeautifulSoup
import requests

estado=raw_input('Estado: ').lower()
cidade=raw_input('Cidade: ')
cidade=cidade[0].upper()+cidade[1::].lower()

site = 'http://www.tempoagora.com.br/previsao-do-tempo/'+estado+'/'+cidade
print '>> Site:',site,'\n'
r = requests.get(site)
soup = BeautifulSoup(r.text, "html5lib")

print '\n======[ Previsao do Tempo: ]======'
for ul in soup.find_all('ul', {'class': 'dsp-table day-info'}):
    for li in ul.find_all('li'):
        print li.text.replace("\t", " ").replace("\r", "").replace("\n", "")

print '\n======[ Proximas horas: ]======'
for ul in soup.find_all('ul', {'class': 'dsp-table next-hours-list'}):
    for li in ul.find_all('li'):
        print li.text.replace("\t", " ").replace("\r", "").replace("\n", "")  