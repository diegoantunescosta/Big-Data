#include<stdio.h>

int main()
{
float c, f;

printf("Digite a temperatura em graus Celsius: ");
scanf("%f",&c);

f = 1.8 * c + 32;

printf("A temperatura em Fahrenheit é :%.1f",f);


return 0;
}
