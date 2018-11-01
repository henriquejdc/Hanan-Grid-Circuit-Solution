#!/usr/bin/env python
# -*- coding: utf-8 -*-
from arv_int import consulta
#Obstacles
obst_x = []
obst_y = []

#Grafo vazio para prim tamanho 0-5 posições
prim = []
prim_resultante = []

def codigo_id(atual_x,atual_y):
    codigo = str(atual_x)+ str(atual_y)
    return codigo

def adiciona_queue(graph_cp_x, graph_cp_y, vert_x, vert_y,raiz):
    pos_x = graph_cp_x.index(vert_x)
    pos_y = graph_cp_y.index(vert_y)
    if(pos_x-1 > -1): #COLOCAR CONDIÇÃO Q SE EXISTE NA QUEUE, TROCAR PELO MENOR
            if (codigo_id(graph_cp_x[pos_x-1],vert_y) in prim[5]):
                posicao = prim[5].index(codigo_id(graph_cp_x[pos_x-1],vert_y))
                if consulta(raiz,vert_x,vert_y) and consulta(raiz,graph_cp_x[pos_x-1], vert_y):
                    prim[2][posicao]= 0
                    prim[3][posicao]=  vert_x
                    prim[4][posicao]=  vert_y
                if(vert_x - graph_cp_x[pos_x-1] < prim[2][posicao]):
                    prim[2][posicao]= vert_x - graph_cp_x[pos_x-1]
                    prim[3][posicao]=  vert_x
                    prim[4][posicao]=  vert_y
            else:
                #condição de obstaculo
                prim[0].append(graph_cp_x[pos_x-1])
                prim[1].append(vert_y)
                if consulta(raiz,vert_x,vert_y) and consulta(raiz,graph_cp_x[pos_x-1], vert_y):
                    custo_aresta = 0
                else:
                    custo_aresta =  vert_x - graph_cp_x[pos_x-1]
                prim[2].append(custo_aresta)
                prim[3].append(vert_x)
                prim[4].append(vert_y)
                #verifcar se é componente
                prim[5].append(codigo_id(graph_cp_x[pos_x-1],vert_y))

    #ir pra direita
    auxiliar = len(graph_cp_x)
    if(pos_x+1 < auxiliar):
        if (codigo_id(graph_cp_x[pos_x+1],vert_y) in prim[5]):
            posicao = prim[5].index(codigo_id(graph_cp_x[pos_x+1],vert_y))
            if consulta(raiz,vert_x,vert_y) and consulta(raiz,graph_cp_x[pos_x+1], vert_y):
                prim[2][posicao]= 0
                prim[3][posicao]=  vert_x
                prim[4][posicao]=  vert_y
            if(graph_cp_x[pos_x+1] - vert_x < prim[2][posicao]):
                prim[2][posicao]= graph_cp_x[pos_x+1] - vert_x
                prim[3][posicao]=  vert_x
                prim[4][posicao]=  vert_y
        else:
        #condição de obstaculo
            prim[0].append(graph_cp_x[pos_x+1])
            prim[1].append(vert_y)
            if consulta(raiz,vert_x,vert_y) and consulta(raiz,graph_cp_x[pos_x+1], vert_y):
                custo_aresta = 0
            else:
                custo_aresta =  graph_cp_x[pos_x+1] - vert_x
            prim[2].append(custo_aresta)
            prim[3].append(vert_x)
            prim[4].append(vert_y)
            prim[5].append(codigo_id(graph_cp_x[pos_x+1],vert_y))
    #para baixo
    if(pos_y-1 > -1):
        if (codigo_id(vert_x,graph_cp_y[pos_y-1]) in prim[5]):
            posicao = prim[5].index(codigo_id(vert_x,graph_cp_y[pos_y-1]))
            if consulta(raiz,vert_x,vert_y) and consulta(raiz,vert_x, graph_cp_y[pos_y-1]):
                prim[2][posicao]= 0
                prim[3][posicao]=  vert_x
                prim[4][posicao]=  vert_y
            elif(vert_y - graph_cp_y[pos_y-1]< prim[2][posicao]):
                prim[2][posicao]= vert_y - graph_cp_y[pos_y-1]
                prim[3][posicao]=  vert_x
                prim[4][posicao]=  vert_y
        else:
        #condição de obstaculo
            prim[0].append(vert_x)
            prim[1].append(graph_cp_y[pos_y-1])
            if consulta(raiz,vert_x,vert_y) and consulta(raiz,vert_x, graph_cp_y[pos_y-1]):
                custo_aresta = 0
            else:
                custo_aresta = vert_y - graph_cp_y[pos_y-1]
            prim[2].append(custo_aresta)
            prim[3].append(vert_x)
            prim[4].append(vert_y)
            prim[5].append(codigo_id(vert_x,graph_cp_y[pos_y-1]))
    #para cima
    auxiliar = len(graph_cp_y)
    if(pos_y+1 < auxiliar):
        if (codigo_id(vert_x,graph_cp_y[pos_y+1]) in prim[5]):
            posicao = prim[5].index(codigo_id(vert_x,graph_cp_y[pos_y+1]))
            if consulta(raiz,vert_x,vert_y) and consulta(raiz,vert_x, graph_cp_y[pos_y+1]):
                prim[2][posicao]= 0
                prim[3][posicao]=  vert_x
                prim[4][posicao]=  vert_y
            if(graph_cp_y[pos_y+1] - vert_y < prim[2][posicao]):
                prim[2][posicao] =  graph_cp_y[pos_y+1] - vert_y
                prim[3][posicao] =  vert_x
                prim[4][posicao] =  vert_y
        else:
        #condição de obstaculo
            prim[0].append(vert_x)
            prim[1].append(graph_cp_y[pos_y+1])
            if consulta(raiz,vert_x,vert_y) and consulta(raiz,vert_x, graph_cp_y[pos_y+1]):
                custo_aresta = 0
            else:
                custo_aresta = graph_cp_y[pos_y+1] - vert_y
            prim[2].append(custo_aresta)
            prim[3].append(vert_x)
            prim[4].append(vert_y)
            prim[5].append(codigo_id(vert_x,graph_cp_y[pos_y+1]))

def adiciona_resultante(atual_x, atual_y, custo,pai_x,pai_y):

    prim_resultante[0].append(atual_x)
    prim_resultante[1].append(atual_y)
    prim_resultante[2].append(custo)
    prim_resultante[3].append(pai_x)
    prim_resultante[4].append(pai_y)
    prim_resultante[5].append(codigo_id(atual_x,atual_y))


def PRIM(graph_cp_x, graph_cp_y, vert_x, vert_y, raiz):
    menor_custo = 0
    pos_menor = 0
    adiciona_queue(graph_cp_x, graph_cp_y, vert_x, vert_y, raiz)

    while (len(prim[0])!=0):
        menor_custo = min(prim[2])
        pos_menor = prim[2].index(menor_custo)

        resultado = codigo_id(prim[0][pos_menor],prim[1][pos_menor])

        if not resultado in prim_resultante[5]:
            adiciona_resultante(prim[0][pos_menor],prim[1][pos_menor],prim[2][pos_menor],prim[3][pos_menor],prim[4][pos_menor])
            vert_x = prim[0][pos_menor]
            vert_y = prim[1][pos_menor]
            adiciona_queue(graph_cp_x, graph_cp_y, vert_x, vert_y, raiz)
            for i in range(6):
                del prim[i][pos_menor]
        else:
            for i in range(6):
                del prim[i][pos_menor]
