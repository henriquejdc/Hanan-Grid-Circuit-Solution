#!/usr/bin/env python
# -*- coding: utf-8 -*-
x = []
y = []
z = []

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
        else:
            if(pontos[0]=="RoutedVia"):
                print("R")
                bondary = pontos[1]
                print(bondary[1])
            else:
                print("RS")
                bondary = pontos[1]
                print(bondary)
                print(bondary[1])
                z.append(int(bondary[1]))
arq.close()
