#include <stdio.h>

int main () 
{
    int i;
   printf("\nDe 0 a 100 usando o for \n");
    for (int i= 1;i<= 100; i++)
    {
    printf("%d\n",i);
    }


    printf("\nDe 0 a 100 usando o WHILE \n");
	i=0;
    while(i <= 100)
    {
    printf("%d\n ",i);
    i++;
    }

    printf("\nDe 0 a 100 usando o DO WHILE \n");
    i=0;
    do 
    {
      printf("%d\n", i );
      i++;
    }
    while (i<100);
  

return 0;
}
