idade = int (input("Digite sua idade: "))

if idade <= 4:
    print("Você não pode participar da natação")    
if idade >= 5 and idade <= 7:
    print("Sua categoria é Infantil A")
if idade >= 8  and idade <=11:
    print("Sua categoria é Infantil B")
if idade >= 12 and idade <=13:
    print("Sua categoria é Juvenil A")
if idade >= 14 and idade <=17:
    print("Sua categoria é Juvenil B ")
if idade >= 18:
    print("Sua categoria é adulto")