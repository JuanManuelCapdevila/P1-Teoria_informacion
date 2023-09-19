import math

def entropiaF(prob_independientes,array):
    i=0
    prob_salida=[0] * len(array[0])
    entropia=0
    while(i < len(array[0])):
        j=0
        while(j < len(array[0])):
            prob_salida[i]+=prob_independientes[j]*(1/array[j][i])
            j+=1
        i+=1

    i=0
    while(i < len(array[0])):
        entropia+=prob_salida[i]*math.log2(1/prob_salida[i])
        i+=1

    return entropia

def entropiaEquivocacion(prob_independientes,array):

    entropia=0
    i=0

    while(i < len(array[0])):
        j=0
        while(j < len(array[0])):
            entropia-=prob_independientes[i]*(1/array[i][j])*math.log2(1/array[i][j])
            j+=1
        i+=1

    return entropia

def info_mutua(prob_independientes,array):

    entropiaFuente=entropiaF(prob_independientes,array)
    equivocacion=entropiaEquivocacion(prob_independientes,array)

    return (entropiaFuente - equivocacion)

def canalUniforme(capacidad_max, array):
    i = 0
    prob_independientes = []
    while (i < len(array[0])):
        prob_independientes.append(1 / len(array[0]))
        i+=1

    return prob_independientes


def canalNoUniforme2(capacidad_max, array):
    prob_max=[0] * 2
    aux=[0] * 2
    max=0
    indexA=0
    indexB=1

    a=0.01
    while((1-a) >= 0):
        aux[indexA]=a
        aux[indexB]=1-a
        if((capacidad_max - info_mutua(aux,array)) < (capacidad_max - max)):
            max=info_mutua(aux,array)
            prob_max[indexA]=aux[indexA]
            prob_max[indexB]=aux[indexB]
        a+=0.01

    return prob_max

def canalNoUniforme3(capacidad_max, array):
    prob_max=[0] * 3
    aux=[0] * 3
    max=0
    indexA=0
    indexB=1
    indexC=2


    b=0.01
    while(b < 1):
        a=0.01
        while((1-a-b) > 0):
            aux[indexA]=a
            aux[indexB]=b
            aux[indexC]=1-a-b
            if((capacidad_max - info_mutua(aux,array)) < (capacidad_max - max)):
                max=info_mutua(aux,array)
                prob_max[indexA]=aux[indexA]
                prob_max[indexB]=aux[indexB]
                prob_max[indexC]=aux[indexC]
            a+=0.01
        b+=0.01

    return prob_max

def canalNoUniforme4(capacidad_max, array):
    prob_max=[0] * 4
    aux=[0] * 4
    max=0
    indexA=0
    indexB=1
    indexC=2
    indexD=3


    c=0.01
    while(c < 1):
        b=0.01
        while(b < 1):
            a=0.01
            while((1-a-b-c) > 0):
                aux[indexA]=a
                aux[indexB]=b
                aux[indexC]=c
                aux[indexD]=1-a-b-c
                if((capacidad_max - info_mutua(aux,array)) < (capacidad_max - max)):
                    max=info_mutua(aux,array)
                    prob_max[indexA]=aux[indexA]
                    prob_max[indexB]=aux[indexB]
                    prob_max[indexC]=aux[indexC]
                    prob_max[indexD]=aux[indexD]
                a+=0.01
            b+=0.01
        c+=0.01

    return prob_max

def main():
    r = int(input("Tipo de canal: "))
    n = int(input("Numero de entradas: "))
    prob_condicionales = [[0] * n for _ in range(n)]  # matriz ---> [n][n] llena de 0s
    prob_independientes=[]
    i = 0

    while (i < n):
        j = 0
        while (j < n):
            prob_condicionales[i][j] = float(input("Ingrese [" + str(i) + "][" + str(j) + "]: "))
            j += 1
        i += 1

    capacidad_max = math.log2(n)

    if (r == 1):
        prob_independientes = canalUniforme(capacidad_max, prob_condicionales)
        i = 0

    else:
        i = 0
        if(n==2):
            prob_independientes = canalNoUniforme2(capacidad_max, prob_condicionales)
        elif(n==3):
            prob_independientes = canalNoUniforme3(capacidad_max, prob_condicionales)
        elif(n==4):
            prob_independientes = canalNoUniforme4(capacidad_max, prob_condicionales)
        else:
            print("Andate a tu casa")


    while (i < len(prob_independientes)):
        print("Probabilidad independiente de [", i, "]", prob_independientes[i])
        i += 1


main()
