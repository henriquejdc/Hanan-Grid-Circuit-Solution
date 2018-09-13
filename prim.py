#!/usr/bin/env python
# -*- coding: utf-8 -*-
# grafo completo x e y, no prim x e y e preços das arestas, vertice atual x e y, componentes,tipo pai
#type 1 é componente e 0 nao componente

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
        if i % 2 == 0 and x > atual_x and x <= prox_x:and :
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
            custo_aresta =  graph_cp_x[pos_x+1]
            prim[2].append(custo_aresta)
            prim[3].append(vert_x)
            prim[4].append(vert_y)
    #para baixo
    if(pos_y-1 > -1):
        #condição de obstaculo
            prim[0].append(graph_cp_y[pos_y-1])
            prim[1].append(vert_x)
            custo_aresta = vert_y - graph_cp_x[pos_y-1]
            prim[2].append(custo_aresta)
            prim[3].append(vert_x)
            prim[4].append(vert_y)
    #para cima
    auxiliar = len(graph_cp_y)
    if(pos_y+1 < auxiliar):
        #condição de obstaculo
            prim[0].append(graph_cp_y[pos_y+1])
            prim[1].append(vert_x)
            custo_aresta = graph_cp_x[pos_y+1] - vert_y
            prim[2].append(custo_aresta)
            prim[3].append(vert_x)
            prim[4].append(vert_y)
            prim[5].append(0)

def adiciona_resultante(atual_x, atual_y, custo, pai_x,pai_y):
    prim_resultante[0].append(atua_x[0])
    prim_resultante[1].append(atual_y[0])
    prim_resultante[2].append(custo)
    prim_resultante[3].append(pai_x)
    prim_resultante[4].append(pai_y)

    if(atual_x>atual_y):
        prim_resultante[5].append("x"+str(atual_x+atual_y))
    if(atual_x<atual_y)):
        prim_resultante[5].append("y"+str(atual_x+atual_y))
    if(atual_x==atual_y):
        prim_resultante[5].append("xy"+str(atual_x+atual_y))


def PRIM(graph_cp_x, graph_cp_y, vert_x, vert_y, vert_comp):
    menor_custo = 0
    pos_menor = 0
    custos = [-1, -1 , -1 , -1]
    #FAZER A VERIFICAÇÃO DE OBSTACULO ENTRE OS PONTOS OU PONTO NO OBSTACULO
    adiciona_queue(graph_cp_x, graph_cp_y, vert_x, vert_y, vert_comp)

    while len(prim[0]!=0):
        menor_custo = min(prim[2])
        pos_menor = prim[2].index(menor_custo)

        if(prim[0][pos_menor]>prim[1][pos_menor]):
            resultado = ("x"+str(atual_x[0]+atual_y[0]))
        if(prim[0][pos_menor]<prim[1][pos_menor]):
            resultado = ("y"+str(atual_x[0]+atual_y[0]))
        if(prim[0][pos_menor]==prim[1][pos_menor]):
            resultado = ("xy"+str(atual_x[0]+atual_y[0]))

        if resultado in prim_resultante[5]:
            adiciona_resultante(prim[0][pos_menor],prim[1][pos_menor],prim[3][pos_menor],vert_x,vert_y)
            vert_x = prim[0][pos_menor]
            vert_y = prim[1][pos_menor]
            del prim[0][pos_menor]
            del prim[1][pos_menor]
            del prim[2][pos_menor]
            del prim[3][pos_menor]
            del prim[4][pos_menor]
            del prim[5][pos_menor]
            adiciona_queue(graph_cp_x, graph_cp_y, vert_x, vert_y, vert_comp):

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
            list = []
            for num in range(2):
                list1 = []
                list.append(list1)
            for w in range(layers):
                layer.append(list)
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
for bond in layer:
    for lay in bond:
        lay = sorted(set(lay))
    termos_x = bond[0]
    termos_y = bond[1]

componentes = []
for numerado in range(2):
    list1 = []
    componentes.append(list1)

componentes[0] = com_x
componentes[1] = com_y

for numerados in range(6):
    list1 = []
    if(numerados!=5)prim.append(list1)
    prim_resultante.append(list1)

adiciona_resultante(com_x[0],com_y[0],0,-1,-1)
PRIM(termos_x, termos_y, com_x[0], com_y[0], componentes)
