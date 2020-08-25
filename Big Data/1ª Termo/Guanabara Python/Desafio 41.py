idade = int(input( 'Digite sua idade:'))

if idade >=0 and idade <= 9 :
    print('Sua categoria é MIRIM')
if idade >=10 and idade <=14:
    print('Sua categoria é INFANTIL')
if idade >=15 and idade <=19:
    print('Sua categoria é JUNIOR')
if idade == 20:
    print('Sua categoria é SENIOR')
if idade > 20:
    print('Sua categoria é MASTER')