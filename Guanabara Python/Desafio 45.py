import random

print("1- Papel\n2- Tesoura\n3- Pedra ")
num = int(input('Escolha uma Opção  '))
sorteio = random.randint(0, 2)
print("JOKEEEEEEEEMPÔÔÔ...")

if sorteio == 1:
    print("A maquina escolheu PAPEL")
if sorteio == 2:
    print("A maquina escolheu TESOURA")
if sorteio == 3:
    print("A maquina escolheu PEDRA")
if num == sorteio:
    print('Você Empatou :D'.format(sorteio))
if num == 1 and sorteio == 2: 
    print( "Você escolheu PAPEL x TESOURA\nPERDEUUUUUUUUUUUUU!!!" )
if num == 1 and sorteio == 3: 
    print( "Você escolheu PAPEL x TESOURA\n GANHOUUUUUUUUUUUU!!!" )
if num == 3 and sorteio == 1: 
    print( "Você escolheu PEDRA x PAPEL\nPERDEUUUUUUUUUUUUU!!!" )
if num == 3 and sorteio == 2: 
    print( "Você escolheu PEDRA x TESOURA\n GANHOUUUUUUUUUUUU!!!" )
if num == 2 and sorteio == 3: 
    print( "Você escolheu TESOURA x PEDRA\nPERDEUUUUUUUUUUUUU!!!" )
if num == 2 and sorteio == 1: 
    print( "Você escolheu TESOURA x PAPEL\n GANHOUUUUUUUUUUUU!!!" )