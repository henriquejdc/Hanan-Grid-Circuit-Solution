def new_node(nivel,x, y):
    maximo = [x[1],y[1]]
    list = [nivel, x,  y, maximo, [], []]
    return list

def consult_arv(raiz, x, y):
    if(x[1]>raiz[3][0]):
        raiz[3][0] = x[1]
    if(y[1]>raiz[3][1]):
        raiz[3][1] = y[1]

    if(raiz[0] == 0):
        if(y[0]<raiz[2][0]):
            if not raiz[4]:
                raiz[4] = new_node(1,x,y)
            else:
                consult_arv(raiz[4],x, y)
        else:
            #print('y,dir')
            if not raiz[5]:
                raiz[5] = new_node(1,x,y)
            else:
                consult_arv(raiz[5],x, y)
    else:
        if(x[0]<raiz[1][0]):
            if not raiz[4]:
                raiz[4] = new_node(0,x,y)
            else:
                consult_arv(raiz[4],x, y)
        else:
            if not raiz[5]:
                raiz[5] = new_node(0,x,y)
            else:
                consult_arv(raiz[5],x, y)


def arv_int(componentes):
    comp = componentes
    x = 0
    while x < len(componentes):
        if x == 0:
            raiz = new_node(0,comp[x][0],comp[x][1]) #tipo pai, x, y, maximos xy e esqerda direita
        else:
            consult_arv(raiz,comp[x][0],comp[x][1])
        x = x + 1
    return raiz

def consulta(raiz,px,py):
    x = raiz

    while((x != []) and not ((x[1][0]<=px and x[1][1]>=px) and (x[2][0]<=py and x[2][1]>=py))):
        esquerda = x[4]
        if(x[4]!=[] and (esquerda[3][0]>=px and esquerda[3][1]>=py)):
            x = x[4]
        else:
            x = x[5]
    if(x != []):
        return 1;
    else:
        return 0;
