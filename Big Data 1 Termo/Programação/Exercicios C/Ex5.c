#include <stdio.h>
#include <string.h>

int main()
{
    char sigla[2];
    while(1)
    {
        printf("Digite seu estado: ");
        scanf("%s",sigla);

        if(!strcmp(sigla, "rj"))
        {
            printf(" Voce é Carioca\n");
        }
        else
        {
            if(!strcmp(sigla, "sp"))
            {
                printf("você é Paulista\n");
            }
            else
            {
                if(!strcmp(sigla, "mg"))
                {
                    printf("você é Mineiro\n");
                }
                else
                {
                    printf(" Você é de outro estado  !\n");
                }
            }
        }
        return 0;
    }
}
