nota1 = int ( input("Digite a nota do aluno P1: "))
nota2 = int ( input("Digite a nota do aluno P2: "))
prese = int ( input ("Digite a quantidade de faltas:"))
aulas = int ( input ("Digite o total de aulas"))

media = (nota1 + nota2) /2
faltas= prese / aulas
print (faltas)
if (media >= 7 and faltas <= 0.25 ):
    print ("Aprovado")
else :
    print("Reprovado")



