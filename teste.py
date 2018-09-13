num = [3,1,2,2,3 ,3]
num1 = len(num)
print num1
print 4%2
test = []
prim = []
for numerados in range(3):
    list1 = []
    prim.append(list1)

prim[0].append(2)
prim[0].append(1)
prim[0].append(2)

prim[1].append(2)
prim[1].append(1)
prim[1].append(3)

if(prim[0][0]>prim[1][0]):
    prim[2].append("x"+str(prim[1][0]+prim[0][0]))
if(prim[0][0]<prim[1][0]):
    prim[2].append("y"+str(prim[1][0]+prim[0][0]))
if(prim[0][0]==prim[1][0]):
    prim[2].append("xy"+str(prim[1][0]+prim[0][0]))

if "y5":
    print("ESSA MERDA")
