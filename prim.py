#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FALTA ARRUMAR ARRASTAS/VALORES, VERIFICAÇÃO COMPONENTES E OBSTACULOS
#Obstacles
obst_x = []
obst_y = []
dist_obj = 5

#Grafo vazio para prim tamanho 0-5 posições
prim = []
prim_resultante = []
def verificar_obstaculo_esq(atual_x, atual_y, prox_x, prox_y):
    i = 0
    for x in obst_x:
        if i % 2 == 0 and x < atual_x and x >= prox_x:
            if atual_y > obst_y[i] and atual_y <= obst_y[i+1]:
                return 1
    i = i+1
def verificar_obstaculo_dir(atual_x, atual_y, prox_x, prox_y):
    i = 0
    for x in obst_x:
        if i % 2 == 0 and x > atual_x and x <= prox_x:
            if (atual_y > obst_y[i] and atual_y <= obst_y[i+1]) :
                return 1
    i = i+1
def verificar_obstaculo_cima(atual_x, atual_y, prox_x, prox_y):
    i = 0
    for y in obst_y:
        if i % 2 == 0 and y > atual_y and y <= prox_y:
            if atual_x > obst_x[i] and atual_x <= obst_x[i+1]:
                return 1
    i = i+1
def verificar_obstaculo_embaixo(atual_x, atual_y, prox_x, prox_y):
    i = 0
    for y in obst_y:
        if i % 2 == 0 and y < atual_y and y >= prox_y:
            if atual_x > obst_x[i] and atual_x <= obst_x[i+1]:
                return 1
    i = i+1

def ser_componente(componentes, vert_x, vert_y):
    print "1"

def adiciona_queue(graph_cp_x, graph_cp_y, vert_x, vert_y, vert_comp):
    pos_x = graph_cp_x.index(vert_x)
    pos_y = graph_cp_y.index(vert_y)

    if(pos_x-1 > -1):
            #condição de obstaculo
            prim[0].append(graph_cp_x[pos_x-1])
            prim[1].append(vert_y)
            #verifcar se é componente
            custo_aresta =  vert_x - graph_cp_x[pos_x-1]
            prim[2].append(custo_aresta)
            prim[3].append(vert_x)
            prim[4].append(vert_y)
    #ir pra direita
    auxiliar = len(graph_cp_x)
    if(pos_x+1 < auxiliar):
        #condição de obstaculo
            prim[0].append(graph_cp_x[pos_x+1])
            prim[1].append(vert_y)
            custo_aresta =  graph_cp_x[pos_x+1] - vert_x
            prim[2].append(custo_aresta)
            prim[3].append(vert_x)
            prim[4].append(vert_y)
    #para baixo
    if(pos_y-1 > -1):
        #condição de obstaculo
            prim[0].append(vert_x)
            prim[1].append(graph_cp_y[pos_y-1])
            custo_aresta = vert_y - graph_cp_y[pos_y-1]
            prim[2].append(custo_aresta)
            prim[3].append(vert_x)
            prim[4].append(vert_y)
    #para cima
    auxiliar = len(graph_cp_y)
    if(pos_y+1 < auxiliar):
        #condição de obstaculo
            prim[0].append(vert_x)
            prim[1].append(graph_cp_y[pos_y+1])
            custo_aresta = graph_cp_y[pos_y+1] - vert_y
            prim[2].append(custo_aresta)
            prim[3].append(vert_x)
            prim[4].append(vert_y)

def adiciona_resultante(atual_x, atual_y, custo,pai_x,pai_y):

    prim_resultante[0].append(atual_x)
    prim_resultante[1].append(atual_y)
    prim_resultante[2].append(custo)
    prim_resultante[3].append(pai_x)
    prim_resultante[4].append(pai_y)

    if(atual_x>atual_y):
        prim_resultante[5].append("x"+str(atual_x+atual_y))
    if(atual_x<atual_y):
        prim_resultante[5].append("y"+str(atual_x+atual_y))
    if(atual_x==atual_y):
        prim_resultante[5].append("xy"+str(atual_x+atual_y))


def PRIM(graph_cp_x, graph_cp_y, vert_x, vert_y, vert_comp):
    menor_custo = 0
    pos_menor = 0
    #FAZER A VERIFICAÇÃO DE OBSTACULO ENTRE OS PONTOS OU PONTO NO OBSTACULO
    adiciona_queue(graph_cp_x, graph_cp_y, vert_x, vert_y, vert_comp)

    while (len(prim[0])!=0):
        menor_custo = min(prim[2])
        pos_menor = prim[2].index(menor_custo)

        if(prim[0][pos_menor]>prim[1][pos_menor]):
            resultado = ("x"+str(prim[0][pos_menor]+prim[1][pos_menor]))
        if(prim[0][pos_menor]<prim[1][pos_menor]):
            resultado = ("y"+str(prim[0][pos_menor]+prim[1][pos_menor]))
        if(prim[0][pos_menor]==prim[1][pos_menor]):
            resultado = ("xy"+str(prim[0][pos_menor]+prim[1][pos_menor]))

        if not resultado in prim_resultante[5]:
            adiciona_resultante(prim[0][pos_menor],prim[1][pos_menor],prim[2][pos_menor],prim[3][pos_menor],prim[4][pos_menor])
            vert_x = prim[0][pos_menor]
            vert_y = prim[1][pos_menor]
            adiciona_queue(graph_cp_x, graph_cp_y, vert_x, vert_y, vert_comp)
        else :
            posicao = prim_resultante[5].index(resultado)
            if prim_resultante[2][posicao] > prim[2][pos_menor]:
                #for i in range(6):
                    #del prim_resultante[i][posicao]
                adiciona_resultante(prim[0][pos_menor],prim[1][pos_menor],prim[2][pos_menor],vert_x,vert_y)

        for i in range(5):
            del prim[i][pos_menor]

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

#Ordena vertices
#####################################
termos_x = []
termos_y = []
for bond in layer:
    bond[0] = sorted(set(bond[0]))
    bond[1] = sorted(set(bond[1]))
    termos_x = termos_x + bond[0]
    termos_y = termos_y + bond[1]
termos_x = sorted(set(termos_x))
termos_y = sorted(set(termos_y))
print termos_x
print termos_y
componentes = []
for numerado in range(2):
    list = []
    componentes.append(list)

componentes[0] = com_x
componentes[1] = com_y

for numerados in range(5):
    list1 = []
    prim.append(list1)

for numerados in range(6):
    list2 = []
    prim_resultante.append(list2)


adiciona_resultante(com_x[0],com_y[0],0,-1,-1)
PRIM(termos_x, termos_y, com_x[0], com_y[0], componentes)

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
