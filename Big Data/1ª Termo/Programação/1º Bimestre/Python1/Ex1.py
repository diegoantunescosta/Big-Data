sal= float (input('Digite o valor do seu salario:'))
aum1= 10
if sal >= 1250 :
    print('Parabéns, seu salario aumento para:R${:.2f}'.format(sal*0.10 +sal))
else:
    print('Parabéns seu salário aumento para :R${:.2f} '.format(sal*0.15 + sal))