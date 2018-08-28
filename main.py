#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Camadas
layer = []
#Borda Left
bondary_lx = 0
bondary_ly = 0
#Borda Right
bondary_rx = 0
bondary_ry = 0

arq = open('case.txt', 'r')
texto = arq.readlines()
for linha in texto :
    pontos = linha.split(" ")
    comentado = pontos[0]

    if(comentado[0] != "#"):
        if(pontos[0]=="Boundary"):
            print(pontos)
            board_left = pontos[2]
            board_right = pontos[3]

            pontos_usado = board_left.split(")")
            pontos_usado1 = pontos_usado[0].split("(")
            pontos_usado_left = pontos_usado1[1].split(",")
            print(pontos_usado_left)
            bondary_lx = int(pontos_usado_left[0])
            bondary_ly = int(pontos_usado_left[1])


            pontos_usado = board_right.split(")")
            pontos_usado1 = pontos_usado[0].split("(")
            pontos_usado_right = pontos_usado1[1].split(",")
            print(pontos_usado_right)
            bondary_rx = int(pontos_usado_right[0])
            bondary_ry = int(pontos_usado_right[1])

        elif(pontos[0]=="MetalLayers"):
            layers = int(pontos[2])
            list = []
            for num in range(2):
                list1 = []
                list.append(list1)
            for w in range(layers):
                layer.append(list)
            #print(layer)
        else:
            if(pontos[0]=="RoutedVia"):
                #print("R")
                bondary = pontos[1]
                #print(bondary)
            else:
                #print("RS")
                bondary = pontos[1]
                #print(bondary)
                #print(bondary[1])
                #z.append(int(bondary[1]))
                #layer[int(bondary[1])-1][0].append(int(bondary[1]))
                pontos_usados = pontos[2].split(",")
                pontos_usados1 = pontos[3].split(",")
                #print(pontos_usados)
                ponto_x = pontos_usados[0].split("(")
                ponto_y = pontos_usados[1].split(")")
                layer[int(bondary[1])-1][0].append(int(ponto_x[1]))
                layer[int(bondary[1])-1][1].append(int(ponto_y[0]))
                #layer[int(bondary[1])][1].append()
                #x.append(int(ponto_x[1]))
                #y.append(int(ponto_y[0]))
                #print(pontos_usados1)
                ponto_x = pontos_usados1[0].split("(")
                ponto_y = pontos_usados1[1].split(")")
                #x.append(int(ponto_x[1]))
                #y.append(int(ponto_y[0]))
                layer[int(bondary[1])-1][0].append(int(ponto_x[1]))
                layer[int(bondary[1])-1][1].append(int(ponto_y[0]))
                #pontos_left = boundary[2]
                #pontos_right = boundary[3]

arq.close()


for bond in layer:
    for lay in bond:
        lay.sort()

for bond in layer:
    print(bond)
#print(layer)
