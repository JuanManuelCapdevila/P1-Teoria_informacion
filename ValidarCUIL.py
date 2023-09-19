from operator import concat

def ValidarCUIL(cuil, s):
    #Verificamos que el sexo indicado al comienzo se corresponda con lo indicado en el CUIL
    if s.upper() == "F" and int(concat(cuil[0],cuil[1])) != 27:
        return -1
    elif s.upper() == "E" and int(concat(cuil[0],cuil[1])) != 30:
        return -1
    elif s.upper() == "M" and int(concat(cuil[0],cuil[1])) != 20:
        return -1
    
    sumatoria = 0
    multiplicador = 6
    #El ultimo digito es verificador del cuil. Este numero se forma a partir de la sumatoria de
    # los digitos XY-DNI multiplicados por la secuencia '6789456789' de forma individual
    # sería: sumatoria = X*6 + Y*7 + DNI[0]*8 + ... + DNI[7]*9
    # luego esta sumatoria calculamos su residuo con respecto a 11 y obtenemos el verificador
    for digito in cuil:
        sumatoria += int(digito) * multiplicador
        if (multiplicador+1) == 10:
            multiplicador = 4
        else:
            multiplicador += 1
    #El número Verificador es XY-DNI-V, valida que el resto del cuil sea correcto
    verificador = sumatoria % 11
    print("Sumatoria = "+ str(sumatoria))
    print("Verificador = " + str(verificador))
    return verificador

if __name__ == "__main__":
    op = 1
    while(str(op) != "0"):
        sexo = input("Determine su sexo M/F o empresa E: ")
        cuil = input("Ingrese su número de CUIL (sin símbolos): ")
        verificador = ValidarCUIL(cuil[:10], sexo)
        if str(verificador) == cuil[-1]:
            print("CUIL válido")
        else:
            print("CUIL invalido")
        op = input("Para finalizar la ejecución ingrese 0, caso contrario presione cualquier tecla: ")