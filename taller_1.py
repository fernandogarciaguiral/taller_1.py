
"""
    Taller # 1 lenguaje de programación 2
    Fernando García Guiral
    Politécnico Colombiano Jaime Isaza Cadavid
"""
import random

#######################################################################################
def ingresar_resistencia(frase):
    """ La función pide al usuario ingresar el valor de la resistencia
    """
    cadena = input(frase).upper()
    return cadena

################################################################################################################
def numero_positivo(mensaje):
    '''
    Recibe el enunciado, lomuestra siempre y cuando sea entero positivo (solo posea números positivos)
    Retorna dato entero
    '''
    while True:
        dato = input(mensaje)
        if dato.isdigit():  # Utilizamos isdigit() para verificar si el dato está compuesto por números del 0 al 9
            if int(dato) >= 0:  # Verificamos si el número es positivo o igual a cero
                break
            else:
                print("Entrada no válida. Solo se permiten ingresar números enteros positivos.")
        else:
            print("Entrada no válida - Solo se permiten ingresar números enteros positivos.")
    return int(dato)
                
########################################################################################################################               
def validar_cadena(cadena):
    """Función que verifica si la cadena termina con 'K' o 'M' y si los caracteres anteriores forman un número válido
       Retorna la parte numérica y la parte literal de la unidad que representa
    """
    if cadena.endswith(('K', 'M')) and cadena[:-1].replace('.', '', 1).isdigit():
        unidad = cadena[-1]
        return True, unidad, cadena
    else:
        return False, None, None
            
##################################################################################################################################################################
def resistencia_ohmios():
    while True:
        es_verdadero, ultimo_caracter, cadena = validar_cadena(ingresar_resistencia('Ingrese el valor de la resistencia con su unidad en "K" o "M" (ejemplo 0.9K): '))
        if es_verdadero == True and ultimo_caracter == 'K':
            resistencia = str(float(cadena[:-1]) * 1000)
            #print(resistencia)
            break
        elif es_verdadero == True and ultimo_caracter == 'M':
            resistencia = str(float(cadena[:-1]) * 1000000)
            #print(resistencia)
            break
        else:
            print('\nDato no válido, intente de nuevo\n')
    return resistencia

###############################################################################################
def ingresar_opcion(menu):
    r_cto = 0
    while True:
        impresiones = []
        opcion = input(menu).lower()
        caracter_permitido = 'abc'
        for char in caracter_permitido:
            if len(opcion) > 1:
                print('\nIngrese solo un valor (a, b ó c): ')
                break        
            else:
                if opcion == 'a':                    
                    resistencia = float(resistencia_ohmios())
                    r_cto += resistencia
                    impresion = f'{fuente + voltaje}|->-|-{serie + str(resistencia)}|->-'
                    impresiones.append(impresion)                    
                    print(impresion)
                    break
                elif opcion == 'b':
                    resistencia1 = float(resistencia_ohmios())
                    resistencia2 = float(resistencia_ohmios())
                    r_total = resistencia1*resistencia2/(resistencia1 + resistencia2)                    
                    r_cto += r_total
                    impresiones.append(f'{fuente + voltaje}|->-|-{paralelo + str(r_total)}|->-')
                    break
                else:
                    return impresiones
                    
menu = """
¿ Qué va conectado a continuación?:

a. Serie
b. Paralelo
c. Cerrar circuito

Ingrese la opción deseada: """                    

impresiones = []
voltaje = 'V'
serie = 'RS'
paralelo = 'RP'
print('\nConstructor de circuitos eléctricos\n')
fuente = str(numero_positivo('Ingrese el valor de la fuente: '))
#print(impresiones.append(f'\n({fuente + voltaje})->-'))
r_sin_tolerancia = ingresar_opcion(menu)
#print(r_sin_tolerancia)




#if __name__ == '__main__':
 #   main()
    