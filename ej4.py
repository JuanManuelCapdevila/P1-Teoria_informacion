''' #Desarrollar una aplicación de software que calcule la Capacidad de Canal de un canal R-ario Uniforme y
#No-Uniforme. El soft debe aceptar como entrada el valor de R que identifica al canal (R= 2 Binario, R=3
#Ternario hasta R=4) los valores de probabilidades condicionales que representan la matriz del canal
#entregando como salida el valor de las probabilidades independientes de cada uno de los símbolos de entrada
#que maximiza la información mutua, esto es, lograr la capacidad de canal. '''


''' entradas: 
    tamaño de canal(2,3,4)
    tipo de canal(uniforme/no uniforme)
    probabilidades(1 fila para uniforme, n filas para no uniforme)
Salida:
    p(ai) para lograr capacidad de canal(p(a)equiprobables en canal uniforme/no uniforme)
    capacidad de canal
 '''
#TODO 


import sys
import math
import random


def calcular_capacidad(matriz, tamanio_canal,tipo_de_canal):
    probabilidades_entrada=[]

    #creo las probabilidades de entrada
    for i in range(tamanio_canal):
        probabilidades_entrada.append(1/tamanio_canal)
    print("Las probabilidades que maximizan la capacidad de canal son: ")
    print(probabilidades_entrada)

          
    #calculo capacidad de canal
    capacidad_canal=0      
    entropia_salida=0 #H(B)
    entropia_equivocacion=0 #H(B/A)
    probabilidades_salida=[] #p(bj)
    probabilidades_condicionales=[] #p(bj/ai)
    
    #calculo H(B)
    for i in range(tamanio_canal):
        pb=0
        for j in range(tamanio_canal):
            if(matriz[j][i]!= 0):#verificar que p(bj/ai) no sea 0
                pb+=probabilidades_entrada[j]*matriz[j][i]
        probabilidades_salida.append(pb)
        entropia_salida+= pb*math.log2(1/pb)

    #calculo H(B/A)
    for i in range(tamanio_canal):
        pcondicional=0
        for j in range(tamanio_canal):
            if(matriz[i][j]!= 0):#verificar que p(bj/ai) no sea 0
                pcondicional+=probabilidades_entrada[i]*matriz[i][j]*math.log2(1/matriz[i][j])
        probabilidades_condicionales.append(pcondicional)
        entropia_equivocacion+= pcondicional
    
    #I(A,B)= H(B)-H(B/A) con p(ai) equiprobables se obtiene la informacion maxima que es la capacidad del canal
    capacidad_canal =entropia_salida-entropia_equivocacion
    print("La capacidad de canal es: "+str(capacidad_canal))
    



def cargar_matriz(matriz,tipo_de_canal,tamanio_canal):
    #canal uniforme    
    if(tipo_de_canal == 1):
        fila_canal=[]
        for i in range(tamanio_canal):
            elemento= float(input("Ingrese el elemento a1"+str(i+1)+": "))
            fila_canal.append(elemento)
        
        if(chequear_fila(fila_canal)):
            matriz.append(fila_canal)
            #construyo la matriz. Realiza rotaciones de elementos de la primer fila 
            for i in range(1,tamanio_canal):#1-tamanio1
                fila_temp = [x for x in range(tamanio_canal)] #crea una fila con tamanio_canal items
                for j in range(tamanio_canal):#0-tamanio Realiza rotaciones de la primer fila
                    indice=(j + i) % tamanio_canal
                    fila_temp[indice]=fila_canal[j]
                matriz.append(fila_temp)
        else:
            print("ERROR EN LAS ENTRADAS")
            return False

    #canal no uniforme
    else:
        for i in range(tamanio_canal):
            fila_canal=[]
            for j in range(tamanio_canal):
                elemento= float(input("Ingrese el elemento a"+str(i+1)+str(j+1)+": "))
                fila_canal.append(elemento)
            if(chequear_fila(fila_canal)):
                matriz.append(fila_canal)
            else:
                print("ERROR EN LAS ENTRADAS")
                return False
    
    mostrar_matriz(matriz)
    return True

def mostrar_matriz(matriz):
    print("\nMatriz resultante")
    for fila  in matriz:
        print(fila)
    print("\n")


def chequear_fila(fila):
    suma=0
    for i in range(len(fila)):
        suma+=fila[i]
    if (suma>=0.99 and suma<=1):
        return True
    else:
       # print("FILAS INVALIDAS")
        return False

    
    
def main():
    matriz=[]
    fila_canal=[]

    tipo_de_canal = int( input("Ingrese el tipo de canal (1 uniforme / 2 no uniforme): "))
    tamanio_canal= int (input("Ingrese el tamaño del canal (2/3/4): "))
    
    if((tamanio_canal>=2 and tamanio_canal<=4)and(tipo_de_canal==1 or tipo_de_canal==2)):
        #Si no hay error en las entradas de la matriz
        if(cargar_matriz(matriz,tipo_de_canal, tamanio_canal)):
            calcular_capacidad(matriz, tamanio_canal, tipo_de_canal)
    else:
        print("ERROR EN LOS PARAMETROS")
        return

if __name__ == "__main__":
    main()





        













