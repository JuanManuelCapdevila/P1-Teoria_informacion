from mimetypes import init

# La clase caracter almacena el caracter en cuestión y su cantidad de apariciones
class Caracter:
    def __init__(self, char):
        self.char = char
        self.apariciones = 1
    
    def incrApariciones(self):
        self.apariciones += 1

    def getApariciones(self):
        return self.apariciones
    
    def getChar(self):
        return self.char