"""
    ALGORITMO PARA CALCULAR LOS COMPONENTES RESISTIVOS EN FUNCIÓN A LAS CAPACITANCIAS Y LOS POLOS Y CEROS DE LA FUNCIÓN DE TRANSFERENCIA PARA UNA PLANTA DE 3ER ORDEN
"""
""" 
Definiendo los coeficientes de la función de transferencia obtenida
Expresión de 2do orden
    A = s^2
    B = S
    C = 1er TI

Expresión de 1er orden
    D = S
    E = 2do TI

TI: Termino Independiente
"""
A = 1
B = 4
C = 3

D = 1
E = 4

G = 100

"""
El objetivo es determinar el valor de resistencias para la implementación
R1=R2=R3=R; R4; R5
Y el valor de capacitancia para C2
"""
# CONSTANTES
caps1 = [10, 33, 47, 100, 330]
C1 = [cap*10**-6  for cap in caps1]

caps3 = [10, 47]
C3 = [cap*10**-6 for cap in caps3]

def calculo_resistencias(A, B, C, D, E, G, C1, C3) :

    R = 3/(C1*B)
    C2 = B**2*C1/(9*C)
    R4 = 1/(G*C1*C2*C3*R**2)
    R5 = 1/(E*C3)

    return [R, C2, R4, R5]

def valores_optimizados(C1, C3) :

    resultados = []

    for i in C1 :
        for j in C3 :
            resultados.append(calculo_resistencias(A, B, C, D, E, G, i, j))

    return resultados            
    
def main() :
    lista_resultados = valores_optimizados(C1, C3)
    print("RESULTADOS")
    print("R, C2, R4, R5")
    i = 0
    for ca1 in C1 :
        for ca3 in C3 :
            print(f'C1 = {ca1}, C3 = {ca3} : {lista_resultados[i]}')
            i = i + 1   

main()

