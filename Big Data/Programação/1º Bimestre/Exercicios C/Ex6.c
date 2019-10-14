#include <stdio.h>
int main ()
{
	float  circulo, raio, area;
	while (1)
	{
	printf("Digite o valor de um raio");
	scanf("%f",&raio);
	
	circulo = raio * raio;
	area = circulo * 3.141592;
	
	printf("O valor da area do circulo é:%f\n",area);
	
	
	}	 
}
