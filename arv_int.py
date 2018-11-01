def new_node(nivel,x, y):
    maximo = [x[1],y[1]]
    minimo = [x[0],y[0]]
    list = [nivel, x,  y, maximo, [], []]
    return list

def consult_arv(raiz, x, y):
    if(x[1]>raiz[4][0]):
        raiz[4][0] = x[1]
    if(y[1]>raiz[4][1]):
        raiz[4][1] = y[1]

    if(x[1]<raiz[3][0]):
        raiz[3][0] = x[1]
    if(y[1]<raiz[3][1]):
        raiz[3][1] = y[1]

    if(raiz[0] == 0):
        if(y[0]<=raiz[2][0]):
            if not raiz[5]:
                raiz[5] = new_node(1,x,y)
            else:
                consult_arv(raiz[5],x, y)
        else:
            if not raiz[6]:
                raiz[6] = new_node(1,x,y)
            else:
                consult_arv(raiz[5],x, y)
    else:
        if(x[0]<=raiz[1][0]):
            if not raiz[5]:
                raiz[5] = new_node(0,x,y)
            else:
                consult_arv(raiz[5],x, y)
        else:
            if not raiz[6]:
                raiz[6] = new_node(0,x,y)
            else:
                consult_arv(raiz[6],x, y)


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
        print(esquerda[1][0],esquerda[3][0])
        if(x[4]!=[] and (esquerda[4][0]>=px and esquerda[4][1]>=py)and(esquerda[3][0]<=px and esquerda[3][1]<=py)):
            print("esq")
            x = x[4]
        else:
            print("dir")
            x = x[5]

    if(x != []):
        return 1;
    else:
        return 0;

def print_a(raiz):
    if(raiz!=[]):
        print((raiz[1],raiz[2],raiz[3]))
        if(raiz[4]!=[]):
            print("esquerda ",raiz[1])
            print_a(raiz[4])
        if(raiz[5]!=[]):
            print("direita ",raiz[1])
            print_a(raiz[5])
