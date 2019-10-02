op = int (input ('Digite 1-Para pagamento a vista\n Digite 2- Para pagamento no crédito\n Qual a forma de pagamento:'))

if op == 1:
    pag1 = float(input('Digite o valor do pagamento:'))
    desc1 = (pag1 * 0.10)
    total1=  pag1 - desc1 
    print ('O pagamento com desconto é R$:{:.2f}'.format(total1))
if op == 2:
    opp = int (input( 'Digite 3 - Para parcelar \n Digite 4 - Pagar a vista no crédito:'))
if opp == 3:
        pag1 = float(input('Digite o valor do pagamento:'))
        parc1 = int (input ('Quantas vezes deseja parcelar seu pagamento:'))
        if parc1 >= 2:
        pag1 = float(input('Digite o valor do pagamento:'))
        parc1 = int (input ('Quantas vezes deseja parcelar seu pagamento:'))
        print ('O valor total é R$:{:.2f}'.format(pag1))
        if parc1 >=3:
if opp == 4:
        pag1 = float(input('Digite o valor do pagamento:'))
        desc1 = (pag1 * 0.05)
        total1=  pag1 - desc1 
        print ('O pagamento com desconto é R$:{:.2f}'.format(total1))

