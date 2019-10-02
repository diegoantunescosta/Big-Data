print ('\033[0;30;41m-=\033[m'*20)
print('Analisador de Triângulos')
print ('\033[1;30;41m-=\033[m'*20)
reta = float (input('Digite um valor para o segmento de reta:'))
retb =  float (input('Digite um valor para o segmento de reta:'))
retc = float (input('Digite um valor para o segmento de reta:'))
print('')

if reta < retb + retc and retb < reta + retc and retc < retb + reta:
    print('É possivel formar um triangulo')
    if reta == retb  == retc:
        print('Você tera um triangulo Equilatero')

    elif reta != retb != retc != reta:
        print('Você tera um Triangulo Escaleno')
    else:
        print('Você tera um Triangulo Isósceles')


else :
    print('É impossivel formar um triângulo')