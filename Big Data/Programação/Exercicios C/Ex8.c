  #include<stdio.h>

    int main ()
{

  float col1,col2, col3,col;

  printf("Digite a colocação da sua equipe: ");
  scanf("%f",&col);
	
  col1 = 0.46 / 12 ;
  col2 = 0.32 / 12 ;
  col3 = 0.22 / 12 ;
	
	
  if (col == 1)
  {
  printf("Parabéns sua equipe vai receber 46%:R$ %f\n",col1);
  }
  if (col == 2)
  {
  printf("Parabéns sua equipe vai receber 32%:R$ %f\n",col2);
  }
  if (col == 3)
  {
  printf("Parabéns sua equipe vai receber 22%:R$ %f \n",col3);
  }

  return 0;
}
    