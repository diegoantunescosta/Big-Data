#include <stdio.h>

int main()
{

float nt1, nt2,faltas;

printf("Digite sua primeira nota:");
scanf("%s",&nt1);

printf("Digite sua segunda nota:");
scanf("%f",&nt2);

printf ("Digite a quantidade de falta:");
scanf("%f",&faltas);

if (((nt1 + nt2)/2 >=7) && ((100 - faltas)* 100)/100 >=75){
  printf ("Aprovado");
}else{
printf( "Reprovado\n");
}
}
