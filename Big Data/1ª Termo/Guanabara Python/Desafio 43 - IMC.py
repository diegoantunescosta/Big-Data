alt=  float (input('Digite sua Altura: '))
peso= float (input('Digite seu peso: '))
##aaaaa
imc1 = alt* alt
imc2 = peso / imc1
print ( '{}'.format(imc2))
if imc2 <= 18.5:
     print('Abaixo do Peso')
if imc2 > 18.5 and imc2 <=25:
    print('Peso Ideal')
if imc2 >25 and imc2 <=30:
    print('Sobrepeso')
if imc2 >30 and imc2 <=40:
    print('Obesidade')
if imc2 > 40:
    print ( 'Obesidade Mórbida')