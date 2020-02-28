#!/usr/bin/env python
# -+- coding : utf-8 -*-
import requests
from lxml import html

page = requests.get("http://br.advfn.com/indicadores/taxa-selic/valores-historicos")
tree = html.fromstring(page.content)
linha = 0
contador = 2

while linha < 219:

    data = list(tree.xpath('//*[@id="section_1"]/table/tbody/tr[%d]/td[1]/text()'% contador))[0]
    vigencia = list(tree.xpath('//*[@id="section_1"]/table/tbody/tr[%d]/td[2]/text()' %contador))[0]
    taxa = list(tree.xpath('//*[@id="section_1"]/table/tbody/tr[%d]/td[3]/text()' %contador))[0]

    inserir = data + " ; " + vigencia + ";" + taxa

    print (inserir)
    linha = linha+1
    contador = contador + 1