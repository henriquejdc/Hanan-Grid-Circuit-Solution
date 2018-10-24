
def new_node(min, max, comp):
    list = [0, min, max, comp, [], []]
    return list

def consult_arv(raiz, min, max, comp):
    if min <= raiz[1]:
        if not raiz[4]:
            raiz[4] = new_node(min,max,comp)
        else:
            
            consult_arv(raiz[4],min, max, comp)
    else:
        if not raiz[5]:
            raiz[5] = new_node(min,max,comp)
        else:

            consult_arv(raiz[5],min, max, comp)

def arv_int(componentes):
    comp = componentes
    x = 0
    while x < len(componentes[0]):
        if x == 0:
            raiz_h = [0,comp[0][x],comp[0][x+1],x-1,[],[]] #filho, ini, fim, n comp
            raiz_v = [0,comp[1][x],comp[1][x+1],x-1,[],[]]
        else:
            consult_arv(raiz_h,comp[0][x],comp[0][x+1],x-1)
            consult_arv(raiz_v,comp[1][x],comp[1][x+1],x-1)
        x = x + 2
    return raiz_h, raiz_v
