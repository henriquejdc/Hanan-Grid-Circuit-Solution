#!/usr/bin/env python
# -*- coding: utf-8 -*-
# grafo completo x e y, no prim x e y e preços das arestas, vertice atual x e y
def PRIM(graph_cp_x, graph_cp_y, graph_prim, vert_x, vert_y, vert_comp):
    pos_x = graph_cp_x.index(vert_x)
    pos_y = graph_cp_y.index(vert_y)

#Utilizando o grafo de prim para retirar os nao arestas componentes
def without_Comp(graph_prim):


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
componentes[0] = com_x
componentes[1] = com_y

#Grafo vazio para prim
prim = []
for numerados in range(3):
    list1 = []
    prim.append(list1)
#todos componentes em x e y, pontos de componente inicial
prim = PRIM(termos_x, termos_y, prim, com_x[0], com_y[0])
