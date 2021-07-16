import numpy as np

arquivo = input("Digite o nome do arquivo")
ref_arquivo = open(arquivo + '.txt','r')

def SplitList(arq):
    i = 0
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
            matriz[i,j] = list[2]
            matriz[j,i] = list[2]
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
            list_adj[i].append([j, list[2]])
            list_adj[j].append([i, list[2]])
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


tes = SplitList(ref_arquivo)
te = ConvertMatriz(tes)

GrauMatriz(te)







