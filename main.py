#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Layers
layer = []
#Bord Left
bondary_coord = []
obst_x = []
obst_y = []
dist_obj = 5

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
                    ponto_x = pontos_usados1[0].split("(")
                    ponto_y = pontos_usados1[1].split(")")
                    layer[int(bondary[1])-1][0].append(int(ponto_x[1]))
                    layer[int(bondary[1])-1][1].append(int(ponto_y[0]))
arq.close()

#Algoritmo de prim para navegar pelos vertices e suas arestas
#Criar como surgir os vertices de encontros de linhas e colunas
#Criar como navegar pelas arestas dos vertices que serao criados


#Prints
#####################################
for bond in layer:
    for lay in bond:
        lay.sort()
print bondary_coord

for bond in layer:
    print(bond)

print obst_x
print obst_y
