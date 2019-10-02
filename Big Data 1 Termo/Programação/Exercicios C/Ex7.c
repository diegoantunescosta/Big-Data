	#include <stdio.h>

	int main ()
	{

	char nome[50];
    int quant, i;
	
		printf("Digite seu nome : ");
		scanf("%[^\n]", nome);	

		printf("Quantas vezes deseja repetir seu nome na tela ");
        scanf("%d",&quant);

        for (i = 1; i <= quant; i++)
        {

          printf("%s\n",nome);

        }
		return 0;
	}