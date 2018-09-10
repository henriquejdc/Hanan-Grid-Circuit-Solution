#!/usr/bin/env python
# -*- coding: utf-8 -*-
# grafo completo x e y, no prim x e y e preços das arestas, vertice atual x e y, componentes,tipo pai
#type 1 é componente e 0 nao componente
def PRIM(graph_cp_x, graph_cp_y, graph_prim, vert_x, vert_y, vert_comp,type_pai,custo_r):
    pos_x = graph_cp_x.index(vert_x)
    pos_y = graph_cp_y.index(vert_y)
    menor_custo = 0
    pos_menor
    custos = [-1, -1 , -1 , -1]
    #ir pra esquerda
    if(pos_x-1 > -1):
        if (graph_cp_x[pos_x-1] in graph_prim[0]):
            pos_yy = graph_prim[0].index(graph_cp_x[pos_x-1])
            if(vert_y == graph_prim[1][pos_yy])):

        else :
            graph_prim[0].append(graph_cp_x[pos_x])
            graph_prim[1].append(vert_y)
            graph_prim[2].append(graph_cp_x[pos_x-1])
            graph_prim[3].append(vert_y)
            custo_aresta =  graph_cp_x[pos_x-1] - vert_x
            graph_prim[4].append(custo_aresta)
            custo_r1 = custo_r + custo_arest
            graph_prim[5].append(custo_r1)
            custos[0] = custo_r1 + custo_r
    #ir pra direita
    if(pos_x+1 < len(graph_cp_x-1)):
        if (graph_cp_x[pos_x+1] in graph_prim[0]):
            pos_yy = graph_prim[0].index(graph_cp_x[pos_x+1])
            if(vert_y == graph_prim[1][pos_yy])):

        else :
            graph_prim[0].append(graph_cp_x[pos_x])
            graph_prim[1].append(vert_y)
            graph_prim[2].append(graph_cp_x[pos_x+1])
            graph_prim[3].append(vert_y)
            custo_aresta =  graph_cp_x[pos_x+1] - vert_x
            graph_prim[4].append(custo_aresta)
            custo_r2 = custo_r + custo_arest
            graph_prim[5].append(custo_r1)
            custos[0] = custo_r2 + custo_r
    #para baixo
    if(pos_y-1 > -1):
        if (graph_cp_y[pos_y-1] in graph_prim[1]):
            pos_xx = graph_prim[1].index(graph_cp_y[pos_y-1])
            if(vert_x == graph_prim[1][pos_xx])):

        else :
            graph_prim[0].append(graph_cp_y[pos_y])
            graph_prim[1].append(vert_x)
            graph_prim[2].append(graph_cp_y[pos_y-1])
            graph_prim[3].append(vert_x)
            custo_aresta =  graph_cp_x[pos_y-1] - vert_y
            graph_prim[4].append(custo_aresta)
            custo_r3 = custo_r + custo_arest
            graph_prim[5].append(custo_r1)
            custos[0] = custo_r3 + custo_r
    #para cima
    if(pos_y+1 < len(graph_cp_y-1)):
        if (graph_cp_y[pos_y+1] in graph_prim[1]):
            pos_xx = graph_prim[1].index(graph_cp_y[pos_y+1])
            if(vert_x == graph_prim[1][pos_xx])):

        else :
            graph_prim[0].append(graph_cp_y[pos_y])
            graph_prim[1].append(vert_x)
            graph_prim[2].append(graph_cp_y[pos_y+1])
            graph_prim[3].append(vert_x)
            custo_aresta =  graph_cp_x[pos_y-1] - vert_y
            graph_prim[4].append(custo_aresta)
            custo_r3 = custo_r + custo_arest
            graph_prim[5].append(custo_r1)
            custos[0] = custo_r3 + custo_r

    while(custos[0] > 0 and custos[1] > 0 and custos[2] > 0 and custos[3] > 0):
        i = 0
        for num in custos:
            i++
            if(num<menor_custo and num>0)
                pos_menor = i
                menor_custo = num
        prim()
    return graph_prim
#Utilizando o grafo de prim para retirar os nao arestas componentes
#def without_Comp(graph_prim):


#Layers
layer = []
#Bord Left
bondary_coord = []
#Obstacles
obst_x = []
obst_y = []
dist_obj = 5
#Vias
vias_bondary = []
vias_x = []
vias_y = []
#Components
com_x = []
com_y = []

arq = open('case.txt', 'r')
texto = arq.readlines()

for linha in texto :
    pontos = linha.split(" ")
    comentado = pontos[0]

    #Ignore Comments
    if(comentado[0] != "#"):
        if(pontos[0]=="Boundary"): #bondary
            #print(pontos)
            board_left = pontos[2]
            board_right = pontos[3]

            pontos_usado = board_left.split(")")
            pontos_usado1 = pontos_usado[0].split("(")
            pontos_usado_left = pontos_usado1[1].split(",")
            bondary_coord.append(int(pontos_usado_left[0]))
            bondary_coord.append(int(pontos_usado_left[1]))
            pontos_usado = board_right.split(")")
            pontos_usado1 = pontos_usado[0].split("(")
            pontos_usado_right = pontos_usado1[1].split(",")
            bondary_coord.append(int(pontos_usado_right[0]))
            bondary_coord.append(int(pontos_usado_right[1]))

        elif(pontos[0]=="MetalLayers"): #Which Layers
            layers = int(pontos[2])
            list = []
            for num in range(2):
                list1 = []
                list.append(list1)
            for w in range(layers):
                layer.append(list)
        else:
            if(pontos[0]=="RoutedVia"): #Don't know
                bondary = pontos[1]
                pontos_usados = pontos[2].split(",")
                ponto_x = pontos_usados[0].split("(")
                ponto_y = pontos_usados[1].split(")")
                vias_bondary.append(int(bondary[1]))
                vias_x.append(int(ponto_x[1]))
                vias_x.append(int(ponto_y[0]))
            else:#Shapes and Obstacle

                if(pontos[0]=="Obstacle"):
                    bondary = pontos[1]
                    pontos_usados = pontos[2].split(",")
                    pontos_usados1 = pontos[3].split(",")
                    ponto_x = pontos_usados[0].split("(")
                    ponto_y = pontos_usados[1].split(")")
                    layer[int(bondary[1])-1][0].append(int(ponto_x[1])+dist_obj)
                    layer[int(bondary[1])-1][1].append(int(ponto_y[0])+dist_obj)
                    obst_x.append(int(ponto_x[1]))
                    obst_y.append(int(ponto_y[0]))
                    ponto_x = pontos_usados1[0].split("(")
                    ponto_y = pontos_usados1[1].split(")")
                    layer[int(bondary[1])-1][0].append(int(ponto_x[1])+dist_obj)
                    layer[int(bondary[1])-1][1].append(int(ponto_y[0])+dist_obj)
                    obst_x.append(int(ponto_x[1]))
                    obst_y.append(int(ponto_y[0]))

                else:
                    bondary = pontos[1]
                    pontos_usados = pontos[2].split(",")
                    pontos_usados1 = pontos[3].split(",")
                    ponto_x = pontos_usados[0].split("(")
                    ponto_y = pontos_usados[1].split(")")
                    layer[int(bondary[1])-1][0].append(int(ponto_x[1]))
                    layer[int(bondary[1])-1][1].append(int(ponto_y[0]))
                    com_x.append(int(ponto_x[1]))
                    com_y.append(int(ponto_y[0]))
                    ponto_x = pontos_usados1[0].split("(")
                    ponto_y = pontos_usados1[1].split(")")
                    layer[int(bondary[1])-1][0].append(int(ponto_x[1]))
                    layer[int(bondary[1])-1][1].append(int(ponto_y[0]))
                    com_x.append(int(ponto_x[1]))
                    com_y.append(int(ponto_y[0]))
arq.close()

#Algoritmo de prim para navegar pelos vertices e suas arestas
#Criar como surgir os vertices de encontros de linhas e colunas
#Criar como navegar pelas arestas dos vertices que serao criados

#Ordena vertices
#####################################
for bond in layer:
    for lay in bond:
        lay.sort()
    termos_x = bond[0]
    termos_y = bond[1]

componentes = []
for numerado in range(2):
    list1 = []
    componentes.append(list1)

componentes[0] = com_x
componentes[1] = com_y

#Grafo vazio para prim
prim = []
for numerados in range(6):
    list1 = []
    prim.append(list1)
#todos componentes em x e y, pontos de componente inicial
prim[0].append(com_x[0])
prim[1].append(com_y[0])
prim[2].append(com_x[0])
prim[3].append(com_y[0])
prim[4].append(0)
prim[5].append(0)

prim = PRIM(termos_x, termos_y, prim, com_x[0], com_y[0], componentes, 1,0)
