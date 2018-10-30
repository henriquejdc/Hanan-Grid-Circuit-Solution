import sys
from prim import *
from random import shuffle
from arv_int import *
#Bord Left
bondary_coord = []

#Vias
vias_bondary = []
vias_x = []
vias_y = []
#Components
com_x = []
com_y = []
com_x1 = []
com_y1 = []
#Distancia dos obstaculos
dist_obj = 0

termos_x = []
termos_y = []

#arq = open(param[1], 'r')
arq = open('caset.txt', 'r')
texto = arq.readlines()

for linha in texto :
    pontos = linha.split(" ")
    comentado = pontos[0]

    #Ignore Comments
    if(comentado[0] != "#"):
        if(pontos[0]=="Boundary"): #bondary
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

        elif(pontos[0]=="Spacing"): #Which Layers
            dist_obj = int(pontos[2])

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
                    if not int(ponto_x[1])+dist_obj in termos_x:
                        termos_x.append(int(ponto_x[1])+dist_obj)
                    if not int(ponto_y[0])+dist_obj in termos_y:
                        termos_y.append(int(ponto_y[0])+dist_obj)
                    obst_x.append(int(ponto_x[1]))
                    obst_y.append(int(ponto_y[0]))
                    ponto_x = pontos_usados1[0].split("(")
                    ponto_y = pontos_usados1[1].split(")")
                    if not int(ponto_x[1])+dist_obj in termos_x:
                        termos_x.append(int(ponto_x[1])+dist_obj)
                    if not int(ponto_y[0])+dist_obj in termos_y:
                        termos_y.append(int(ponto_y[0])+dist_obj)
                    obst_x.append(int(ponto_x[1]))
                    obst_y.append(int(ponto_y[0]))

                else:
                    x = [0,0]
                    y = [0,0]
                    bondary = pontos[1]
                    pontos_usados = pontos[2].split(",")
                    pontos_usados1 = pontos[3].split(",")
                    ponto_x = pontos_usados[0].split("(")
                    ponto_y = pontos_usados[1].split(")")
                    if not int(ponto_x[1])in termos_x:
                        termos_x.append(int(ponto_x[1]))
                    if not int(ponto_y[0]) in termos_y:
                        termos_y.append(int(ponto_y[0]))
                    x[0] = int(ponto_x[1])
                    y[0] = int(ponto_y[0])
                    com_x.append(int(ponto_x[1]))
                    com_y.append(int(ponto_y[0]))
                    ponto_x = pontos_usados1[0].split("(")
                    ponto_y = pontos_usados1[1].split(")")
                    if not int(ponto_x[1]) in termos_x:
                        termos_x.append(int(ponto_x[1]))
                    if not int(ponto_y[0]) in termos_y:
                        termos_y.append(int(ponto_y[0]))
                    com_x.append(int(ponto_x[1]))
                    com_y.append(int(ponto_y[0]))
                    x[1] = int(ponto_x[1])
                    y[1] = int(ponto_y[0])
                    com = [x,y]
                    com_x1.append(com)
arq.close()

termos_x.sort()
termos_y.sort()

for numerados in range(6):
    list1 = []
    prim.append(list1)

for numerados in range(2):
    list = []
    componentes.append(list)

shuffle(com_x1)

componentes[0] = com_x
componentes[1] = com_y

raiz = arv_int(com_x1)
print raiz


for numerados in range(6):
    list2 = []
    prim_resultante.append(list2)


adiciona_resultante(com_x[0],com_y[0],0,-1,-1)
PRIM(termos_x, termos_y, com_x[0], com_y[0],raiz)

arq = open('out', 'w')
imprimir = []
for numeradosss in range(len(prim_resultante[0])):
    list1 = []
    imprimir.append(list1)

for test in prim_resultante:
    contador_1 = 0
    for test2 in test:
        imprimir[contador_1].append(test2)
        contador_1 = contador_1 + 1

for numeradosss in range(len(prim_resultante[0])):
    arq.writelines(str(imprimir[numeradosss])+"\n")

arq.close()
