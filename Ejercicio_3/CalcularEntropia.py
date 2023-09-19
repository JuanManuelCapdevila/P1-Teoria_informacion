from math import log2
import os
from Caracter import Caracter

def BuscaCaracter(lista, char):
    for elem in lista:
        if elem.getChar() == char:
            return elem
    return None

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    os.chdir(path)
    contadorCaracteres = 0
    lista = []
# Para probar distintos archivos debemos cambiar el nombre y puede ser
# ArchivoDeTexto.txt
# ArchivoDeTexto2.txt
# Ejecutable.exe
# TextoConFormato.pdf
    with open(os.path.join(path+"\\Comprimido.zip"), "rb") as file:
        for data in file:
            contadorCaracteres += len(data)
            for byte1 in list(bytes(data)):
                aux = BuscaCaracter(lista, chr(byte1))
                if aux == None:
                    lista.append(Caracter(chr(byte1)))
                else:
                    aux.incrApariciones()
    
    #Calculamos la entropía H(B) = Sumtoria(p(bj)*log2(1/p(bj))) 
    # donde p(bj) -> x && log2(1/p(bj)) -> y
    entropia = 0
    x = 0
    y = 0
    for b in lista:
        x = b.getApariciones() / contadorCaracteres
        y = log2(1/x)
        entropia += x*y

    print(f"La entropía del archivo seleccionado es: {entropia}")
    print(f"La redundancia del código es: {1 - entropia/log2(len(lista))}")