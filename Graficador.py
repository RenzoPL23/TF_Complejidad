import matplotlib.pyplot as plt
import matplotlib.collections

def str2pair(x):
    """
    Recibe una cadena como '4,5' y retorna una tupla (4, 5)
    """
    nums = x.split(',')
    return int(nums[0]), float(nums[1])

def LeeLAP2LAP(filename):
    """
    Funcion lee un archivo que contiene un grafo en formato de lista de adyacencia
    con pesos y retorna una lista de adyacencia con pesos
    """
    G = []
    file = open(filename)
    for line in file:
        G.append([str2pair(x) for x in line.split(' ')])
    return G
def LeerCPS(CPS):
    cps=open(CPS,"r")
    G = []
    for line in cps:
        a,b=[float(i) for i in line.split(',')]
        G.append((a,b))
    return G
#X,Y DE CPS
cps=LeerCPS("SortedY_DS_CReg.csv")
#RUTA
ways=LeeLAP2LAP("DS_CReg_10_cercanos.csv")
segs=[]
#for i in range(2):
 #   cpslej[i][0],cpslej[i][1]= (cpslej[i][0]+86)*(800/22),(cpslej[i][1])*(650/20)+10
# Note that the patches won't be added to the axes, instead a collection will

fig, ax = plt.subplots()

cpsIter=iter(cps)       
for v in ways:
    xi,yi=next(cpsIter)
    for way in v:
        segs.append([(xi,yi),cps[way[0]]])
#Graficado
lines = matplotlib.collections.LineCollection(segs,linewidths=0.5,colors='blue',linestyle='solid')
coll = matplotlib.collections.EllipseCollection(3,3,0,offsets=cps,color='red', units='points',
                                                transOffset=ax.transData)
ax.add_collection(lines)
ax.add_collection(coll)


ax.margins(0.01)
plt.grid(True)
plt.show()
