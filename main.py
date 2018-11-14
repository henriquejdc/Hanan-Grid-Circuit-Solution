import sys
from prim import *
from random import shuffle
from arv_int import *
#Bord Left

print (sys.argv)
bondary_coord = []

#Vias
vias_bondary = []
vias_x = []
vias_y = []
#Components
com_x1 = []
#Distancia dos obstaculos
dist_obj = 0

termos_x = []
termos_y = []

resultado_final = []

arq = open(sys.argv[1], 'r')
#arq = open('caset.txt', 'r')
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
                    ponto_x = pontos_usados1[0].split("(")
                    ponto_y = pontos_usados1[1].split(")")
                    if not int(ponto_x[1]) in termos_x:
                        termos_x.append(int(ponto_x[1]))
                    if not int(ponto_y[0]) in termos_y:
                        termos_y.append(int(ponto_y[0]))
                    x[1] = int(ponto_x[1])
                    y[1] = int(ponto_y[0])
                    com = [x,y]
                    com_x1.append(com)
arq.close()

termos_x.sort()
termos_y.sort()

for numerados in range(8):
    list1 = []
    prim.append(list1)

shuffle(com_x1)
com_x = com_x1[0][0][0]
com_y = com_x1[0][1][0]

#print(com_x1)
raiz = arv_int(com_x1)
#print('\n')
#print_a(raiz)

for numerados in range(8):
    list2 = []
    prim_resultante.append(list2)

for numerados in range(3):
    list3 = []
    prim_gg.append(list3)

initial = consulta(raiz,com_x1[0][0][0], com_x1[0][1][0], com_x1[0][0][1], com_x1[0][1][1])
prim_gg[0].append(0)
prim_gg[1].append(initial)
prim_gg[2].append([-1,-1])

print(prim_gg)
del com_x1

adiciona_resultante(com_x,com_y,0,-1,-1,[-1,-1],0)
PRIM(termos_x, termos_y, com_x, com_y,raiz, initial)

arq = open(sys.argv[2], 'w')
sorteada = []
for test in range(len(prim_gg[2])):
    sorteada = sorteada + prim_gg[2]
    print(prim_gg[2])
    #arq.writelines(str(prim_gg[0][test])+" "+str(prim_gg[1][test])+str(prim_gg[2][test])+"\n")
sorted(set(sorteada))
arq.writelines(str(sorteada)+"\n")
arq.close()
