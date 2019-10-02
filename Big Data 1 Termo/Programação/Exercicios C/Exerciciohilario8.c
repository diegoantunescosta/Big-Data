#include <stdio.h>


int dobro( int a)

{ printf("Entrei na função");
	return a * 2;
}	

int main()
{
	int a;

printf("o numero real e:");
scanf("%d", &a);

printf("\n o dobro e: %d \n",dobro(a));
}