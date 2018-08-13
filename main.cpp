#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct board{ //Struct das variaveis A,B...
    int cod_left;
    int cod_right;
    struct board* next;
} board;

typedef struct object{ //Struct das variaveis A,B...
    int cod_left;
    int cod_right;
    struct board* this_board;
    struct object* next;
} object;


int main(){


	return 0; 
}