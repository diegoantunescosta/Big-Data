
op = int (input ('Digite 1-Para pagamento a vista\n Digite 2- Para pagamento no crédito\n Qual a forma de pagamento:'))

if op == 1:
    pag1 = float(input('Digite o valor do pagamento:'))
    desc1 = (pag1 * 0.10)
    total1=  pag1 - desc1 
    print ('O pagamento com desconto é R$:{:.2f}'.format(total1))
if op == 2:
    op = int (input('Digite 3 - Para parcelar \n Digite 4 - Pagar a vista no crédito:'))
    if op == 3:
        pag2 = float (input('Digite o valor do pagamento:'))
        parc2 = float (input ('Quantas vezes deseja parcelar seu pagamento:'))
        total2 = (pag2 / parc2)
        print ('O pagamento com desconto é R$:{:.2f}'.format(total2))
        if parc2 >= 2:
        pag3 = float(input('Digite o valor do pagamento:'))
        parc3 = int (input ('Quantas vezes deseja parcelar seu pagamento:'))
        total3 = (pag2 / parc2)
        acres3 = (total * 1.2)
        print ('O valor total é R$:{:.2f}'.format(acres3))
        #if parc1 >=3:
#if opp == 4:
 #       pag4 = float(input('Digite o valor do pagamento:'))
  #      desc4 = (pag4 * 0.05)
   #     total4=  pag4 - desc4 
    #    print ('O pagamento com desconto é R$:{:.2f}'.format(total1))