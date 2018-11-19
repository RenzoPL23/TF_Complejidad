import math as mt 
import heapq as hq
def asd(x):
    num = x.split(',')
    return int(num[0]),float(num[1])

def LeerListAP(filename):
    G=[]
    file= open(filename,'r',encoding='utf8')
    for line in file:
        G.append([asd(x) for x in line.split( )])
    return G

def prim(G,s,t):
    n = len(G)
    dist = [mt.inf]*n
    path = [-1]*n
    visited = [False]*n
    dist[s]=0
    q = []
    hq.heappush(q, (0, s))
    dist[0] = 0
    while len(q) > 0:
        _, u = hq.heappop(q)
        if visited[u]: continue
        visited[u] = True
        if u ==t: break
        for v, w in G[u]:
            if not visited[v] and w < dist[v]:
                dist[v] = w
                path[v] = u
                hq.heappush(q, (w, v))
    return path, dist
def CrearTxt(filename,p):
    file = open(filename,"w")
    n = len(p)
    for i in range(n):
        file.write(str(p[i]))
        file.write('\n')
    file.close()
def combinacion(c1,c2):
    for i in range(len(c1)):
        if c1[i] == -1:
            c1[i] = c2[i]
    return c1
#DS_CDist_10_cercanos.csv 1678
#DS_CProv_10_cercanos.csv 171
#DS_CReg_10_cercanos.csv 25
#LAP2.txt 145224

def Camino(filename,s,t):
    G = LeerListAP(filename)
    p,d=prim(G,s,t-1)
    lenG = len(G)
    indexaux=t-1
    camino=[-1]*lenG
    while(True):
        camino[indexaux]=p[indexaux]
        indexaux=p[indexaux]
        if p[indexaux]==-1:
            break
    return camino

#camino = Camino('LAP2.txt',0,145224)
camino1 = Camino('DS_CReg_10_cercanos.csv',15,25)
camino2 = Camino('DS_CReg_10_cercanos.csv',0,15+1)
ca=combinacion(camino1,camino2)
#CDis.txt
#CProv.txt
#CReg.txt
#CResto.txt
CrearTxt('CReg1.txt',ca)