import numpy as np

arquivo = input("Digite o nome do arquivo")
ref_arquivo = open(arquivo + '.txt','r')

def SplitList(arq):
    teste = []
    for linha in arq:
        valores = linha.split()
        teste.append(valores)
    return teste

def ConvertMatriz(lists):
    index = True
    for list in lists:
        i = int(list[0])
        j = int(list[1])
        if index:
            matriz = np.zeros((i+1,i+1),dtype='uint8')
            index = False
        else:
            matriz[i,j] = int(list[2])
            matriz[j,i] = int(list[2])
    return matriz

def ConvertList(lists):
    index = True
    for list in lists:
        i = int(list[0])
        j = int(list[1])
        if index:
            list_adj = [[]for _ in range(i+1)]
            index = False
        else:
            x = int(list[2])
            list_adj[i].append([j, x])
            list_adj[j].append([i, x])
    return list_adj

def Grau(grau):
    max = grau[0]
    min = grau[0]
    index = 0
    for g in grau:
        if g > max:
            #grau maximo e vertice do grau
            max = g
            verticeMax = index
        if g < min :
            # grau minimo e vertice do grau
            min = g
            verticeMin = index
        index += 1
    print("Maior grau: ", max, " Vertice: ", verticeMax)
    print("Menor grau: ", min, " Vertice: ", verticeMin)
    GrauMedio(grau,max)

def GrauMedio(grau,max):
    grauMedio = []
    totalGrauMedio = 0
    for g in grau:
        existe = True
        for gMedio in grauMedio:
            if g == gMedio:
                existe = False
        if existe:
            grauMedio.append(g)
            totalGrauMedio += g
    grauMedioTotal = totalGrauMedio / len(grau)
    print("Grau medio: ",grauMedioTotal)
    FrequenciaGrau(grau,grauMedio,max)

def FrequenciaGrau(grau,grauMedio,max):
    x = len(grau)
    frequencia = [0 for _ in range(max+1)]
    frequenciaTotal = [0 for _ in range(max+1)]
    for g in grau:
        for gMedio in grauMedio:
            if g == gMedio:
                frequencia[gMedio] += 1
    index = 0
    for freq in frequencia:
        frequenciaTotal[index] = (100 * freq)/x
        index += 1

    print("Frequencia relativa:")
    index = 0
    for freq in frequenciaTotal:
        if freq > 0.0:
            print("Grau ", index,": ", freq)
        index += 1

def GrauList(lists):
    grau = []
    for list in lists:
        grau.append(len(list))
    Grau(grau)

def GrauMatriz(matriz):
    n = len(matriz)
    grau = [[] for _ in range(n)]
    index = 0
    for mat in matriz:
        g = 0
        for m in mat:
            if(m > 0):
                g += 1
        grau[index] = g
        index += 1
    Grau(grau)

def BuscaLarguraLista(G, s):
    desc = [0 for _ in range(len(G))]
    nivel = [-1 for _ in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(Q) != 0:
        u = Q.pop(0)
        print("teste",u)
        n = nivel[u]+1
        for v in G[u]:
            if desc[v[0]] == 0:
                Q.append(v[0])
                R.append(v[0])
                desc[v[0]] = 1
            if nivel[v[0]] == -1 or nivel[v[0]] >= n:
                nivel[v[0]] = n
    print("Vertice:Nivel")
    for i in range(len(desc)):
        if nivel[i] >= 0:
            print(i, ": ", nivel[i])

def BuscaLarguraMatriz(G, s):
    desc = [0 for _ in range(len(G))]
    nivel = [-1 for _ in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(Q) != 0:
        u = Q.pop(0)
        n = nivel[u]+1
        index = 0
        for m in G[u]:
            if m > 0:
                if desc[index] == 0:
                    Q.append(index)
                    R.append(index)
                    desc[index] = 1
                if nivel[index] == -1 or nivel[index] >= n:
                    nivel[index] = n
            index += 1
    print("Vertice:Nivel")
    for i in range(len(desc)):
        if nivel[i] >= 0:
            print(i, ": ", nivel[i])

def BuscaProfundidade (G,s):
    desc = [0 for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for v in G[u]:
            if desc[v] == 0:
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                break
        if desempilhar:
            S.pop()


tes = SplitList(ref_arquivo)
te = ConvertMatriz(tes)
BuscaLarguraMatriz(te,0)
