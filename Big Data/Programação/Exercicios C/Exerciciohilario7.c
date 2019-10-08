#include<stdio.h>

int main()

{
    float salario,parcela;
    printf("Digite o Valor do seu salario: ");
    scanf("%f",&salario);
    printf("Digite o valor da prestação que deseja pagar: ");
    scanf("%f",&parcela);
  

    
        if (parcela >= salario * 0.2)
        {
        printf("Você não tem direito a emprestimo");

        }
         else
        { 
        printf("Você tem direito a emprestimo");
        }
}
