# HANAN GRID

Preview and implement Optimizer Hanan Grid construction.

# Documentation

Layer = Matriz 3-dimensional das camadas
bondary_coord = Coordenadas da camada

A cada 2 posições é um obstaculo
Primeiro é o ponto inferior e o segundo superior
obst_x = Coordenadas dos obstáculos de X
obst_y = Coordenadas dos obstáculos de Y

dist_obj = distancia dos pontos de Steiner do objeto

Tomar nota que:

Pontos independem de camadas, todas serão feitos juntos,Após sera feito as arestas entre camadas.

Será feito uma árvore entre todos os vértices com a distancia minima entre eles usando prim,
o qual tem adaptações para navegar entre os pontos de Steiner e pontos dentro de um componente,

Quando se adiciona um ponto novo não conhecido na queue e este é componente ou está dentro das arestas de componentes
ele tem custo 0

Logo, serão excluídos pontos que não fazem parte de caminhos entre componentes


time python main.py


###################################################################################################
from random import shuffle
Tornar os pontos pares como lista = [[3,4],[5,6]] e utilizar o shuffle
random.shuffle(lista)
Fazer a arvore por par/impar e guardar o max X e max Y
