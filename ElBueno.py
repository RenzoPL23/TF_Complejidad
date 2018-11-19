#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
def pitagoras(a,b):
    return math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))
def asd(x):
    num = x.split(',') 
    if 'n' in x:
        num[1]=num[1][:len(num[1])-1]
    return [int(num[0]),float(num[1])]
def segundo(G):
    return G[1]
def LeerListAP(filename):
    G=[]
    file= open(filename)
    for line in file:
        G.append(sorted([asd(i) for i in line.split(' ')],key=segundo))
    file.close()
    return G
def LeerListDist(filename):
    G=[]
    file= open(filename)
    for line in file:
        num = line.split(',')
        num[0]=num[0][:len(num[0])-1]
        num[len(num)-1]=num[len(num)-1][:len(num[len(num)-1])-1]
        G.append([float(num[0]),float(num[1])])
    file.close()
    return G
def bellmanford(G, s):
    n = len(G)
    d = [math.inf]*n
    p = [None]*n
    d[s] = 0
    for _ in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    p[v] = u
    return p
def CrearTxt(filename,p):
    file = open(filename,"w")
    n = len(p)
    for i in range(n):
        file.write(str(p[i]))
        file.write('\n')
    file.close()
G=LeerListAP("CDist10.csv")
primernodo=0
primercamino=bellmanford(G,primernodo)
lenG=len(G)

A=LeerListDist("DS_CDist.csv")

indexlejos=0
distancias0=[None]*lenG
distanciasult=[None]*lenG
distancias0[indexlejos]=pitagoras(A[primernodo],A[indexlejos])

for i in range(len(G)):
    
    distancias0[i]=pitagoras(A[primernodo],A[i])
    if(distancias0[indexlejos]<distancias0[i]):
        largo=distancias0[i]
        indexlejos=i
        
distancias0[primernodo]=math.inf

for i in range(len(G)):
    distanciasult[i]=pitagoras(A[indexlejos],A[i])
        
distanciasult[indexlejos]=math.inf
camino=[None]*lenG
indexaux=indexlejos


while(1):
    camino[indexaux]=primercamino[indexaux]
    indexaux=primercamino[indexaux]
    if primercamino[indexaux]==None:
        break
camino[0]=None


##for i in range(lenG):
  ##  print (i)
    ##print(G[i])
nodousado=indexlejos
caminoaux=[None]*len(camino)
def greedy(G,camino,nodousado,nodofinal,n):
    if nodousado==nodofinal:
        print("termino")
        return True
    direccion=0
    n=len(G[0])
    rutas=[None]*n
    for i in range(n):
        rutas[i]=G[nodousado][i][0]
    for i in range(len(rutas)):
        if camino[rutas[i]]==None:
            auxnodousado=nodousado
            camino[rutas[i]]=nodousado
            nodousado=rutas[i]
            if greedy(G,camino,nodousado,nodofinal,n)==True:
                return True
            else:
                camino[rutas[i]]=None
                nodousado=auxnodousado
    return False
n=[0]
for i in camino:
    if i!=None:
        n[0]+=1
print("comienza greedy")
greedy(G,camino,nodousado,primernodo,n)
for i in range(lenG):
    if camino[i]==None:
        camino[i]=-1
print(camino)
print(n[0])
CrearTxt("CDistrito.txt",camino)
    

        
        
        


# In[ ]:





# In[ ]:




