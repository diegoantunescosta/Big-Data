continuar = "s"
totalpedido = 0
pedidoparcial = 0

while (continuar == 's' or continuar == 'S'):

    print('\033[1;32m {:=^40}'.format(' Fatec Burguer '))

    print("Tabela de preços")
    print("Cod 100 - Cachorro Quente R$ 1.20")
    print("Cod 101 - Bauru Simples R$ 1.30")
    print("Cod 102 - Bauru com Ovo R$ 1.30")
    print("Cod 103 - Hamburguer R$ 1.50")
    print("Cod 104 - Cheeseburguer R$ 1.70")
    print("Cod 105 - Suco R$ 1.20")
    print("Cod 106 - Refrigerante R$ 1.20")

    pedido = int(input("Digite seu pedido:"))
    quant = int(input("Digite a quantidade:"))

    if (pedido == 100):
        print("Você escolheu o cachorro quente")
        pedidoparcial = quant * 1.20

    if (pedido == 101):
        print("Você escolheu o Bauru Simples")
        pedidoparcial = quant * 1.30

    if (pedido == 102):
        print("Você escolheu o Bauru Simples")
        pedidoparcial = quant * 1.50

    if (pedido == 103):
        print("Você escolheu o Hamburguer")
        pedidoparcial = quant * 1.20

    if (pedido == 104):
        print("Você escolheu o Chesseburguer")
        pedidoparcial = quant * 1.70

    if (pedido == 105):
        print("Você escolheu o Suco")
        pedidoparcial = quant * 2.20

    if (pedido == 106):
        print("Você escolheu o refrigerante")
        pedidoparcial = quant * 1.00
    totalpedido = totalpedido + pedidoparcial

    continuar = str(input("Para continuar o pedido digite S/N"))
    if (continuar == 'n' or 'N'):
        print("valor Total:", totalpedido)
        break

        print("valor Total:", totalpedido)