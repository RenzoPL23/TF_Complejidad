import matplotlib.pyplot as plt
import matplotlib.collections

def LeerCPS(CPS):
    cps=open(CPS,"r")
    G = []
    for line in cps:
        a,b=[float(i) for i in line.split(',')]
        G.append((a,b))
    return G

def LeerRuta(filename):
    ruta=open(filename,"r")
    path=[]
    for line in ruta:
        path.append(int(line))
    return path

#X,Y DE CPS
cps=LeerCPS('SortedY_DS_CReg.csv')
#RUTA
ways=LeerRuta('CReg.txt')
print(ways)
segs=[]

fig, ax = plt.subplots()

#CONVERTIR LA RUTA EN LISTA DE SEGMENTOS
cpsIter=iter(cps)       
for v in ways:
    xi,yi=next(cpsIter)
    if v!=-1:
        segs.append([(xi,yi),cps[v]])

#Graficado

lines = matplotlib.collections.LineCollection(segs,linewidths=0.5,colors='blue',linestyle='solid')
coll = matplotlib.collections.EllipseCollection(1,1,0,offsets=cps,color='red', units='points',
                                                transOffset=ax.transData)
ax.add_collection(lines)
ax.add_collection(coll)

ax.margins(0.01)
plt.grid(True)
plt.show()


