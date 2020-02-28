    #include<stdio.h>

    int main ()

    {
		
		int i;
        float num, total, soma= 0, media, maior = 0, menor= 10000000;
        
        printf("Quantos numeros deseja digitar? ");
        scanf("%f",&total);

		

        for (i = 0; i<total; i++)
        {
            printf("Digite um numero:");
            scanf("%f", &num);
            soma = soma + num;
			
			if (num > maior )
			{
				maior = num;
			}
			if (num < menor )
			{
				menor = num;
			}
        
       
		}
      
		printf( "valor da soma: %.2f\n",soma);
        
        printf("Quantidade de numeros digitados: %.2f\n",total);
        
        media = soma / total;
                     
        printf("media dos numeros digitados %.2f\n",media);
        
        printf("O maior numero digitado foi: %.2f\n", maior);
        
        printf("O menor numero digitado foi: %.2f", menor);
        
        return 0;
    }