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
    print(pontos[1])
    
    if(pontos[0]=="Boundary"):
        print("B")
    else:
        if(pontos[0]=="RoutedVia"):
            print("R")
        else:
            print("RS")
arq.close()
