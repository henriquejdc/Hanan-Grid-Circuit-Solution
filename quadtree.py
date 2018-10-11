from prim import *

#Bord Left
bondary_coord = []
componentes = []
comp_on =[] #componente oeste norte
comp_os =[] #componente oeste sul
comp_ln =[] #componente leste norte
comp_ls =[] #componente leste sul

def add_quads(n_q,nn_q,xm,xma,ym,yma): #numero do quad, numero do sub quad
    if(n_q==0):
        comp_on[nn_q][0].append(xm)
        comp_on[nn_q][1].append(ym)
        comp_on[nn_q][0].append(xma)
        comp_on[nn_q][1].append(yma)
    if(n_q==1):
        comp_os[nn_q][0].append(xm)
        comp_os[nn_q][1].append(ym)
        comp_os[nn_q][0].append(xma)
        comp_os[nn_q][1].append(yma)
    if(n_q==2):
        comp_ln[nn_q][0].append(xm)
        comp_ln[nn_q][1].append(ym)
        comp_ln[nn_q][0].append(xma)
        comp_ln[nn_q][1].append(yma)
    if(n_q==3):
        comp_ls[nn_q][0].append(xm)
        comp_ls[nn_q][1].append(ym)
        comp_ls[nn_q][0].append(xma)
        comp_ls[nn_q][1].append(yma)

def div_quads():
    x_m = bondary_coord[2]
    y_m = bondary_coord[3]
    x = 0
    while x < len(componentes[0]):
        xm = componentes[0][x]
        xma = componentes[1][x]
        ym = componentes[0][x+1]
        yma = componentes[1][x+1]
        if((xm < x_m/2 or xma < x_m/2) and (ym > y_m/2 or yma>y_m/2)): #in on
            if((xm < x_m/4 or xma < x_m/4) and (ym > y_m/4 or yma>y_m/4)): #in on_0
                add_quads(0,0,xm,xma,ym,yma)
            if((xm < x_m/4 or xma < x_m/4) and (ym < y_m/4 or yma<y_m/4)): #in on_1
                add_quads(0,1,xm,xma,ym,yma)
            if((xm > x_m/4 or xma > x_m/4) and (ym > y_m/4 or yma>y_m/4)): #in on_2
                add_quads(0,2,xm,xma,ym,yma)
            if((xm > x_m/4 or xma > x_m/4) and (ym < y_m/2 or yma<y_m/4)): #in on_3
                add_quads(0,3,xm,xma,ym,yma)
        if((xm < x_m/2 or xma < x_m/2) and (ym < y_m/2 or yma<y_m/2)): #in os
            if((xm < x_m/4 or xma < x_m/4) and (ym > y_m/4 or yma>y_m/4)): #in os_0
                add_quads(1,0,xm,xma,ym,yma)
            if((xm < x_m/4 or xma < x_m/4) and (ym < y_m/4 or yma<y_m/4)): #in os_1
                add_quads(1,1,xm,xma,ym,yma)
            if((xm > x_m/4 or xma > x_m/4) and (ym > y_m/4 or yma>y_m/4)): #in os_2
                add_quads(1,2,xm,xma,ym,yma)
            if((xm > x_m/4 or xma > x_m/4) and (ym < y_m/2 or yma<y_m/4)): #in os_3
                add_quads(1,3,xm,xma,ym,yma)
        if((xm > x_m/2 or xma > x_m/2) and (ym > y_m/2 or yma>y_m/2)): #in ln
            if((xm < x_m/4 or xma < x_m/4) and (ym > y_m/4 or yma>y_m/4)): #in ln_0
                add_quads(2,0,xm,xma,ym,yma)
            if((xm < x_m/4 or xma < x_m/4) and (ym < y_m/4 or yma<y_m/4)): #in ln_1
                add_quads(2,1,xm,xma,ym,yma)
            if((xm > x_m/4 or xma > x_m/4) and (ym > y_m/4 or yma>y_m/4)): #in ln_2
                add_quads(2,2,xm,xma,ym,yma)
            if((xm > x_m/4 or xma > x_m/4) and (ym < y_m/2 or yma<y_m/4)): #in ln_3
                add_quads(2,3,xm,xma,ym,yma)
        if((xm > x_m/2 or xma > x_m/2) and (ym < y_m/2 or yma<y_m/2)): #in ls
            if((xm < x_m/4 or xma < x_m/4) and (ym > y_m/4 or yma>y_m/4)): #in ls_0
                add_quads(3,0,xm,xma,ym,yma)
            if((xm < x_m/4 or xma < x_m/4) and (ym < y_m/4 or yma<y_m/4)): #in ls_1
                add_quads(3,1,xm,xma,ym,yma)
            if((xm > x_m/4 or xma > x_m/4) and (ym > y_m/4 or yma>y_m/4)): #in ls_2
                add_quads(3,2,xm,xma,ym,yma)
            if((xm > x_m/4 or xma > x_m/4) and (ym < y_m/2 or yma<y_m/4)): #in ls_3
                add_quads(3,3,xm,xma,ym,yma)
    x = x + 2
