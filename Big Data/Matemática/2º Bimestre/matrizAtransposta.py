from random import randint
matriza = [[0,0,0],[0,0,0],[0,0,0]]
matrizb = [[0,0,0],[0,0,0],[0,0,0]]
for l in range( 0,3):
    for c in range (0,3):
        num = int (randint(0,10))
        matriza[l][c] = num
        matrizb[c][l] =num
  
print('-=' *30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriza[l][c]:^5}]', end= '')
         
    print()
    
print('-=' *30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matrizb[l][c]:^5}]', end= '')
  
    print()
