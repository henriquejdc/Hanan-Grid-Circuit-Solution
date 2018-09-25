from prim import *

#Layers
layer = []
#Bord Left
bondary_coord = []

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

            for w in range(layers):
                list = []
                layer.append(list)

            for w in range(layers):
                for num in range(2):
                    lista = []
                    layer[w].append(lista)
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
                    if not int(ponto_x[1]+dist_obj) in  layer[int(bondary[1])-1][0]:
                        layer[int(bondary[1])-1][0].append(int(ponto_x[1])+dist_obj)
                    if not int(ponto_y[0]+dist_obj) in  layer[int(bondary[1])-1][1]:
                        layer[int(bondary[1])-1][1].append(int(ponto_y[0])+dist_obj)
                    obst_x.append(int(ponto_x[1]))
                    obst_y.append(int(ponto_y[0]))
                    ponto_x = pontos_usados1[0].split("(")
                    ponto_y = pontos_usados1[1].split(")")
                    if not int(ponto_x[1]+dist_obj) in  layer[int(bondary[1])-1][0]:
                        layer[int(bondary[1])-1][0].append(int(ponto_x[1])+dist_obj)
                    if not int(ponto_y[0]+dist_obj) in  layer[int(bondary[1])-1][1]:
                        layer[int(bondary[1])-1][1].append(int(ponto_y[0])+dist_obj)
                    obst_x.append(int(ponto_x[1]))
                    obst_y.append(int(ponto_y[0]))

                else:
                    bondary = pontos[1]
                    pontos_usados = pontos[2].split(",")
                    pontos_usados1 = pontos[3].split(",")
                    ponto_x = pontos_usados[0].split("(")
                    ponto_y = pontos_usados[1].split(")")
                    if not int(ponto_x[1]) in  layer[int(bondary[1])-1][0]:
                        layer[int(bondary[1])-1][0].append(int(ponto_x[1]))
                    if not int(ponto_y[0]) in  layer[int(bondary[1])-1][1]:
                        layer[int(bondary[1])-1][1].append(int(ponto_y[0]))
                    com_x.append(int(ponto_x[1]))
                    com_y.append(int(ponto_y[0]))
                    ponto_x = pontos_usados1[0].split("(")
                    ponto_y = pontos_usados1[1].split(")")
                    if not int(ponto_x[1]) in  layer[int(bondary[1])-1][0]:
                        layer[int(bondary[1])-1][0].append(int(ponto_x[1]))
                    if not int(ponto_y[0]) in  layer[int(bondary[1])-1][1]:
                        layer[int(bondary[1])-1][1].append(int(ponto_y[0]))
                    com_x.append(int(ponto_x[1]))
                    com_y.append(int(ponto_y[0]))
arq.close()

#Ordena vertices
#####################################
termos_x = []
termos_y = []
for bond in layer:
    bond[0].sort()
    bond[1].sort()
    termos_x = termos_x + bond[0]
    termos_y = termos_y + bond[1]
termos_x = sorted(set(termos_x))
termos_y = sorted(set(termos_y))
#print termos_x
#print termos_y

for numerados in range(6):
    list1 = []
    prim.append(list1)

for numerados in range(2):
    list = []
    componentes.append(list)

componentes[0] = com_x
componentes[1] = com_y


for numerados in range(6):
    list2 = []
    prim_resultante.append(list2)


adiciona_resultante(com_x[0],com_y[0],0,-1,-1)
PRIM(termos_x, termos_y, com_x[0], com_y[0])

arq = open('out.txt', 'w')
teta = []
for numeradosss in range(len(prim_resultante[0])):
    list1 = []
    teta.append(list1)

for test in prim_resultante:
    xxt = 0
    for test2 in test:
        teta[xxt].append(test2)
        xxt = xxt + 1

for numeradosss in range(len(prim_resultante[0])):
    arq.writelines(str(teta[numeradosss])+"\n")

arq.close()

print layer
print componentes
print termos_x
print termos_y
#print obst_x
#print obst_y
