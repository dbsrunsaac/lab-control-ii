"""
    ALGORITMO PARA CALCULAR LOS COMPONENTES RESISTIVOS EN FUNCIÓN A LAS CAPACITANCIAS Y LOS POLOS Y CEROS DE LA FUNCIÓN DE TRANSFERENCIA PARA UNA PLANTA DE 3ER ORDEN
"""

# CONSTANTES
C1 = 10*10**-6
C3 = 47*10**-6
""" 
Definiendo los coeficientes de la función de transferencia obtenida
Expresión de 2do orden
    A = s^2
    B = S
    C = 1er TI
Expresión de 3er orden
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
def calculo_resistencias(A, B, C, D, E, G):
    R = 3/(C1*B)
    C2 = B**2/((C1**3)*9*C)
    R4 = 1/(G*C1*C2*C3*R**2)
    R5 = 1/(E*C3)

    return [R, C2, R4, R5]

def main() :
    resultados = calculo_resistencias(A, B, C, D, E, G)
    print("Los resultados para: R, C2, R4 Y R5 son:")
    for resultado in resultados :
        print(resultado)

main()

