#include<stdlib.h>
#include<stdio.h>
#include<string.h>
void mmc(int num1,int num2,int *resultado){
   int cont=2,dividiu,result=1;
   while (num1!=1 || num2!=1){
         dividiu=0;
         if (num1%cont==0){
            dividiu=1;
            num1=num1/cont;
         }
         if (num2%cont==0){
            dividiu=1;
            num2=num2/cont;
         }
         if (dividiu==0){
           cont++;
         }else{
           result=result*cont;
         }
   } 
   *resultado=result; 
}


main(){
  int a,b,c, next;
  while (next = 1)
  {
  printf("Calculadora de MMC\n");
  printf("Digite um numero:");
  scanf("%d",&a);
  printf("Digite outro numero:");
  scanf("%d",&b);
  mmc(a,b,&c);
  printf("O resultado do MMC é  :%d\n",c);
  printf("Para resolver outro calculo digite 1:");
  scanf("%d",&next);
  }
  
}