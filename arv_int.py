#fazer max e min dos nodos
def new_node(nivel,min, max):
    maximo = max
    list = [nivel, min, max, maximo, [], []]
    return list

def consult_arv(raiz, min, max):
    if(max[0]>raiz[3][0]):
        raiz[3][0] = max[0]
    if(max[1]>raiz[3][1]):
        raiz[3][1] = max[1]

    if(raiz[0] == 0):
        if(min[1]<raiz[1][1]):
            print('y,esq')
            if not raiz[4]:
                raiz[4] = new_node(1,min,max)
            else:
                consult_arv(raiz[4],min, max)
        else:
            print('y,dir')
            if not raiz[5]:
                raiz[5] = new_node(1,min,max)
            else:
                consult_arv(raiz[5],min, max)
    else:
        if(min[0]<raiz[1][0]):
            print('x,esq')
            if not raiz[4]:
                raiz[4] = new_node(0,min,max)
            else:
                consult_arv(raiz[4],min, max)
        else:
            print('x,dir')
            if not raiz[5]:
                raiz[5] = new_node(0,min,max)
            else:
                consult_arv(raiz[5],min, max)


def arv_int(componentes):
    comp = componentes
    x = 0
    while x < len(componentes[0]):
        print(x)
        if x == 0:
            raiz = [0,comp[0][x],comp[1][x],comp[1][x],[],[]] #filho, ini, fim, n comp
        else:
            consult_arv(raiz,comp[0][x],comp[1][x])
        x = x + 1
    return raiz
