#include<stdio.h>

int main ()
{ 	
	int a = 0;
	
	scanf("%i", &a);
	
	for(int x= 1; x <= 10; ++x){
		//1 x 5 =5
		printf("%i\n%i\n%i\n",x,a,x * a);
	}
	return 0;
}
