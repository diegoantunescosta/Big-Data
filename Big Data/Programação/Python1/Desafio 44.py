#Elabore um programa que calcule o valor a ser pago de um produto,
#considerando o seu preço normal, e condição de pagamento:
#- À vista no dinheiro/cheque: 10% de desconto
#- À vista no cartão: 5% de desconto
#- Em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros
vpago = float (input("Digite o valor: "))
avista = vpago - 0.10