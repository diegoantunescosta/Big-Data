#include<stdio.h>

int main ()
{
	int n1,n2,n3;
	
	printf("Entre com o primeiro numero: ");
	scanf("%d",&n1);

	printf("Entre com o primeiro segundo: ");
	scanf("%d",&n2);
	
	printf("Entre com o primeiro terceiro: ");
	scanf("%d",&n3);
	
	if (n1>=n2 && n1>=n3)
	printf("%d e' o maior numero digitado",n1);

	if (n2>=n1 && n2>=n3)
	printf("%d e' o maior numero digitado",n2);

	if (n3>=n1 && n1>=n2)
	printf("%d e' o maior numero digitado",n3);
	
	return 0;
}