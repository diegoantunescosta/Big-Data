#include<stdio.h>
//testedas

int main ()
{
  float ad,sub, div, mult, num1, num2;
  int op;

 
  sub= num1 - num2;
  div= num1 / num2;
  mult= num1* num2;

  printf(" 1 - Adição \n 2 - Subtação \n 3 - Divisão \n 4- Multiplicação\n");

  printf( "\nDigite o número da opção que deseja calcular: ");
  scanf("%d", &op);


  if ( op == 1)

  {

  printf("\nDigite um numero:");
  scanf("%f",&num1);

  printf("\nDigite um numero:");
  scanf("%f",&num2);

  ad = num1 + num2;
  printf("\nResultado: %2.f\n",ad);
  }

  if ( op == 2)

  {

  printf("\nDigite um numero:");
  scanf("%f",&num1);

  printf("\nDigite um numero:");
  scanf("%f",&num2);

  ad = num1 - num2;
  printf("\nResultado: %2.f\n",ad);
  }

  if ( op == 3)

  {

  printf("\nDigite um numero:");
  scanf("%f",&num1);

  printf("\nDigite um numero:");
  scanf("%f",&num2);

  ad = num1 / num2;
  printf("\nResultado: %2.f\n",ad);
  }

if ( op == 4)

  {

  printf("\nDigite um numero:");
  scanf("%f",&num1);

  printf("\nDigite um numero:");
  scanf("%f",&num2);

  ad = num1 * num2;
  printf("\nResultado: %2.f\n",ad);
  }


  return 0;

}