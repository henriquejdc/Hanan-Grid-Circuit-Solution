#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct board{ //Struct das variaveis A,B...
    int cod_left;
    int cod_right;
    struct board* next;
} board;


#define MAXCARACTERES 100

int main(){
  int board_left, board_right;

	FILE * arquivo;
	arquivo = fopen("case.txt","r");

	if(arquivo == NULL){
		printf("Nao foi possivel abrir o arquivo !\n");
		return 1;
	}

	char frase[MAXCARACTERES];

	while(fgets(frase,MAXCARACTERES,arquivo) != NULL){
		printf("%s",frase);
	}

	printf("\n");

	fclose(arquivo);

	return 0;
}
