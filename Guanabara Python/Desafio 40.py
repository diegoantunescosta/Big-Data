nota1= float(input('Digite a nota1:'))
nota2= float(input('Digite a nota2:'))

med1 = (nota1 + nota2) / 2
print ('Media {}'.format(med1))
if med1 < 5.0:
    print('Reprovado')
if med1 >= 5 and med1 <= 6.9:
    print('Recuperação')
if med1 >= 7.0:
    print('Aprovado')