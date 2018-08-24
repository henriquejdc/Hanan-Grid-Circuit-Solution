#!/usr/bin/env python
# -*- coding: utf-8 -*-
x = []
y = []
z = []
board_right = 0
board_left = 0

arq = open('case.txt', 'r')
texto = arq.readlines()
for linha in texto :
    pontos = linha.split(" ")

    if(pontos[0]=="Boundary"):
        print(pontos)
    else:
        if(pontos[0]=="RoutedVia"):
            print("R")
            bondary = pontos[1]
            print(bondary[1])
        else:
            print("RS")
            bondary = pontos[1]
            print(bondary[1])
arq.close()
