#include<stdio.h>

int main ()
{
 float alt, peso ,imc2 ,imc1;

	

    printf("Digite sua altura:\n");
    scanf ("%f",alt);

    printf("Digite sua Peso:\n");
    scanf("%f", peso);

	imc1 = alt * alt;
    imc2 = peso / imc1;

  

    if ( imc2 <= 18.5)
   
    {
        printf( "Abaixo do Peso");
    }

    if ( imc2 > 18.5 && imc2 <= 25)
   
    {
        printf( "Peso Ideal");
    }

    if ( imc2 > 25 && imc2 <= 30)
    {
        printf( "Sobrepeso");
    }
    
    if ( imc2 > 30 && imc2 <= 40)
   
    {
        printf( "Obesidade");
    }
    
    if ( imc2 > 40)
   
    {
        printf( "Obesidade Morbida");
    }

return 0;

}
