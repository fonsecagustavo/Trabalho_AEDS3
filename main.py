import numpy as np

def menu():
    arquivo = input("Digite o nome do arquivo")
    ref_arquivo = open(arquivo + '.txt', 'r')
    arquivo = SplitList(ref_arquivo)

    representa = int(input("Digite 1 para Lista, 2 Para Matriz ou 0 para sair."))
    while representa != 0:
        if representa == 1:
            menuLista(arquivo)
            representa = int(input("Digite 1 para Lista, 2 Para Matriz ou 0 para sair."))
        elif representa == 2:
            menuMatriz(arquivo)
            representa = int(input("Digite 1 para Lista, 2 Para Matriz ou 0 para sair."))
        else:
            representa = int(input("Digite 1 para Lista, 2 Para Matriz ou 0 para sair."))

def menuLista(arquivo):
    lista = ConvertList(arquivo)
    escolha = 1
    while escolha != 0:
        print("1 - Representação")
        print("2 - Informações")
        print("3 - Busca em Grafos: Largura")
        print("4 - Busca em Grafos:  Profundidade")
        print("5 - Componentes Conexos")
        print("0 - Voltar")
        escolha = int(input(""))
        if escolha == 1:
            for lis in lista:
                print(lis)
        elif escolha == 2:
            GrauList(lista)
        elif escolha == 3:
            BuscaLarguraLista(lista,1)
        elif escolha == 4:
            BuscaProfundidadeLista(lista,1)
        elif escolha == 5:
            ComponentesConexasLista(lista)

def menuMatriz(arquivo):
    matriz = ConvertMatriz(arquivo)
    escolha = 1
    while escolha != 0:
        print("1 - Representação")
        print("2 - Informações")
        print("3 - Busca em Grafos: Largura")
        print("4 - Busca em Grafos:  Profundidade")
        print("5 -Componentes Conexos")
        print("0 - Voltar")
        escolha = int(input(""))
        if escolha == 1:
            print(matriz)
        elif escolha == 2:
            GrauMatriz(matriz)
        elif escolha == 3:
            BuscaLarguraMatriz(matriz,1)
        elif escolha == 4:
            BuscaProfundidadeMatriz(matriz,1)
        elif escolha == 5:
            print("Sem")

#transforma os dados em uma lista
def SplitList(arq):
    dados = []
    for linha in arq:
        valores = linha.split()
        dados.append(valores)
    return dados

#Converte os dados em uma matriz de adjacentes
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

#Converte os dados em uma lista de adjacentes
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

#Começa separando quantas conexões cada um tem
#Um para a lista e outro para matriz
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

#chaga os dados e encontra o maior e o menor grau
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

#Econtra o grau medio
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

#E a frequencia de cada grau
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

#Busca em largura para lista de adjacentes
def BuscaLarguraLista(G, s):
    desc = [0 for _ in range(len(G))]
    nivel = [-1 for _ in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(Q) != 0:
        u = Q.pop(0)
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

#Busca em largura para matriz de adjacentes
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

#Busca em profundidade para lista de adjacentes
def BuscaProfundidadeLista (G,s):
    desc = [0 for _ in range(len(G))]
    nivel = [-1 for _ in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        n = nivel[u] + 1
        for v in G[u]:
            if nivel[v[0]] == -1 or nivel[v[0]] >= n:
                nivel[v[0]] = n
            if desc[v[0]] == 0:
                desempilhar = False
                S.append(v[0])
                R.append(v[0])
                desc[v[0]] = 1
                break
        if desempilhar:
            S.pop()
    print("Vertice:Nivel")
    for i in range(len(desc)):
        if nivel[i] >= 0:
            print(i, ": ", nivel[i])

#Busca em profundidade para matriz de adjacentes
def BuscaProfundidadeMatriz (G,s):
    desc = [0 for _ in range(len(G))]
    nivel = [-1 for _ in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        n = nivel[u] + 1
        index = 0
        for v in G[u]:
            if v > 0:
                if nivel[index] == -1 or nivel[index] >= n:
                    nivel[index] = n
                if desc[index] == 0:
                    desempilhar = False
                    S.append(index)
                    R.append(index)
                    desc[index] = 1
                    break
            index += 1
        if desempilhar:
            S.pop()
    print("Vertice:Nivel")
    for i in range(len(desc)):
        if nivel[i] >= 0:
            print(i, ": ", nivel[i])

def BuscaProfundidadeListaConexa(G, s, marca):
    desc = [0 for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    vComp[s]=marca
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for e in G[u]:
            v = e[0]
            if desc[v] == 0:
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                break
        vComp[u]=marca
        if desempilhar:
            S.pop()


def ComponentesConexasLista(G):
    global vComp
    vComp = [0 for i in range(len(G))]
    marca = 0
    for i in range(len(G)):
        if vComp[i] == 0:
            marca= marca + 1
            BuscaProfundidadeListaConexa(G, i, marca)

    print("Componentes Conexas:{}".format(marca))
    n = max(vComp)
    for i in range(1,n+1):
        print("{} vertices".format(vComp.count(i)))

menu()
