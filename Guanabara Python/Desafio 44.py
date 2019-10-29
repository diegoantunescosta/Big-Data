#Elabore um programa que calcule o valor a ser pago de um produto,
#considerando o seu preço normal, e condição de pagamento:
#- À vista no dinheiro/cheque: 10% de desconto
#- À vista no cartão: 5% de desconto
#- Em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros

print(" \n                Formas de pagamento ")
print("\nDigite 1 para pagamento a vista no dinheiro ou cheque:")
print("Digite 2 para pagamento a vista no cartão:")
print("Digite 3 para pagamento parcelado no cartão:")
form = float( input( "Digite a opção de pagamento:"))

if form == 1:
    dinh = float ( input("Digite o valor da compra: "))
    desdin = dinh * 0.10
    print("O valor total é : {}".format( dinh - desdin ))

if  form == 2:
    dinh = float ( input("Digite o valor da compra: "))
    desdin = dinh * 0.05
    print("O valor total é : {}".format( dinh - desdin ))
if form == 3:
    dinh = float ( input("digite o valor da compra: "))
    parc = int (input("Digite o total de parcelas: "))
    parcelado = dinh / parc 
    totalparcial = parcelado * 0.2
    total = totalparcial + parcelado

    if (parc <= 2):
        print("O valor total é : {}".format( dinh ))
        
    else:
        print("Você pagara {} parcelas de R${:.2f}".format( parc, total ))