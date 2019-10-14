#include <stdio.h>

function main ()
{
	float raio,area,PI;
	PI= 3.14159;
	printf("Digite o valor do raio do circulo: ");
	scanf("%f", &raio);
	area= PI*raio*raio;
	printf("Area do circulo com raio %f e' %f\n",raio,area);
}
