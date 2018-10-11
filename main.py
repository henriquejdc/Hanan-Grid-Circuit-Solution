import sys
from prim import *
from quadtree import *

param = sys.argv

#Vias
vias_bondary = []
vias_x = []
vias_y = []
#Components
com_x = []
com_y = []

#Distancia dos obstaculos
dist_obj = 0

termos_x = []
termos_y = []

arq = open(param[1], 'r')
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
                    bondary = pontos[1]
                    pontos_usados = pontos[2].split(",")
                    pontos_usados1 = pontos[3].split(",")
                    ponto_x = pontos_usados[0].split("(")
                    ponto_y = pontos_usados[1].split(")")
                    if not int(ponto_x[1])in termos_x:
                        termos_x.append(int(ponto_x[1]))
                    if not int(ponto_y[0]) in termos_y:
                        termos_y.append(int(ponto_y[0]))
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
arq.close()

termos_x.sort()
termos_y.sort()
#print termos_x
#print termos_y

for cont in range(6):
    list1 = []
    prim.append(list1)
    list2 = []
    prim_resultante.append(list2)

for cont in range(2):
    list = []
    componentes.append(list)

componentes[0] = com_x
componentes[1] = com_y

for cont in range(4):
    v1 = []
    v2 = []
    v3 = []
    v4 = []
    comp_on.append(v1)
    comp_os.append(v2)
    comp_ln.append(v3)
    comp_ls.append(v4)

for t in range(4):
    v1 = []
    v2 = []
    v3 = []
    v4 = []
    v5 = []
    v6 = []
    v7 = []
    v8 = []
    comp_on[t].append(v1)
    comp_os[t].append(v2)
    comp_ln[t].append(v3)
    comp_ls[t].append(v4)
    comp_on[t].append(v5)
    comp_os[t].append(v6)
    comp_ln[t].append(v7)
    comp_ls[t].append(v8)

print comp_os

div_quads()

print comp_os

del componentes
del termos_x
del termos_y

adiciona_resultante(com_x[0],com_y[0],0,-1,-1)
PRIM(termos_x, termos_y, com_x[0], com_y[0])

arq = open('out', 'w')
imprimir = []
for numeradosss in range(len(prim_resultante[0])):
    list1 = []
    imprimir.append(list1)

for test in prim_resultante:
    imprimir[0].append(test[0])
    imprimir[1].append(test[1])
    imprimir[2].append(test[2])
    imprimir[3].append(test[3])
    imprimir[4].append(test[4])
    imprimir[5].append(test[5])

for numeradosss in range(len(prim_resultante[0])):
    arq.writelines(str(imprimir[numeradosss])+"\n")

arq.close()
