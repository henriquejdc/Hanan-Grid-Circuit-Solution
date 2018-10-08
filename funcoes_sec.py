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
