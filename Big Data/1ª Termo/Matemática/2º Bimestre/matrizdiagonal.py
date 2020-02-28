from random import randint
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range( 0,3):
    for c in range (0,3):
        if l == c:
            matriz[l][c] = int (randint(0,10))
        else:
            matriz[l][c] = 0
print('-=' *30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end= '')
    print()
    diag = []
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            diag.append(matriz[i][j])

print('Matriz Diagonal{}'.format(diag))
