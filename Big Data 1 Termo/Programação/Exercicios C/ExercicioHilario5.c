#include <stdio.h>


	int main(void) {
	  float  op, unid, total ;
	printf("Tabela de Opções\n");
    	printf("Cachorro Quente = 100\n");
	printf("Bauru Simples = 101\n");
	printf("Bauru com Ovo = 102\n");
	printf("Hamburguer = 103\n");
	printf("cheeseburguer= 104\n");
	printf("Suco = 105\n");
	printf("Refrigerante = 106\n");
	printf("Digite o codigo da opção: ");
	scanf("%f", &op);	

		if (op == 100)
		{
			printf("Você escolheu um Cachorro Quente - R$ 1.20\n");
    
			printf("Quantas unidades deseja : ");
			scanf("%f", &unid);
			total = unid * 1.20;
		
			
			printf("Você pagara:R$ %.2f\n",total);
		
		}
    	if (op == 101)
		{
			printf("Você escolheu um Bauru Simples - R$ 1.30\n");
     
			printf("Quantas unidades deseja : ");
			scanf("%f", &unid);
			
			total = unid * 1.30;
		
			
			printf("Você pagara:R$ %.2f\n",total);
		
		}
		if (op == 102)
		{
			printf("Você escolheu um Bauru com Ovo - R$ 1.50\n");
     
			printf("Quantas unidades deseja : ");
			scanf("%f", &unid);
			
			total = unid * 1.50;
		
			
			printf("Você pagara:R$ %.2f\n",total);
		
		}
		if (op == 103)
		{
			printf("Você escolheu um Hamburguer - R$ 1.20\n");
     
			printf("Quantas unidades deseja : ");
			scanf("%f", &unid);
			
			total = unid * 1.20;
		
			
			printf("Você pagara:R$ %.2f\n",total);
		
		}
		if (op == 104)
		{
			printf("Você escolheu um Cheeseburguer - R$ 1.70\n");
     
			printf("Quantas unidades deseja : ");
			scanf("%f", &unid);
			
			total = unid * 1.70;
		
			
			printf("Você pagara:R$ %.2f\n",total);
		
		}
		if (op == 105)
		{
			printf("Você escolheu um Suco - R$ 2.20\n");
     
			printf("Quantas unidades deseja : ");
			scanf("%f", &unid);
			
			total = unid * 2.20;
		
			
			printf("Você pagara:R$ %.2f\n",total);
		
		}
		if (op == 106)
		{
			printf("Você escolheu um Refrigerante - R$ 1.00\n");
     
			printf("Quantas unidades deseja : ");
			scanf("%f", &unid);
			
			total = unid * 1.00;
		
			
			printf("Você pagara:R$ %.2f\n",total);
		
		}
  }