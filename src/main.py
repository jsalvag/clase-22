import math
# Escribir una funcion que basado en el radio:
#  calcule la sup de un circulo
#  calcule la circunferencia
#  calcule la sup de una esfera
#  calcule el vol de una esfera

def calcularCircunferencia(radio):
    """
    calcularCircunferencia() -> float

    radio -- radio is in float
    """

    circunferencia = math.pi * 2 * radio

    return circunferencia

def main():
    """
    main() -> None
    """
    myVariable = complex()
    print(myVariable)

    sumatoria(3)
    print(calVolumenParalelepipedo(2, 3, 10))
    print(sumatoria(3))
    print(sumatoriaLambda(3))

    return None


sumatoriaLambda = lambda x: (x * (x + 1)) / 2


def sumatoria(x):
    resultado = (x * (x + 1)) / 2
    return resultado


def calVolumenParalelepipedo(x, y, z):
    # global resultado
    resultado = x * y * z
    return resultado


# print(resultado)

# Esto sera una constante
complex_zero = {0, 0}


def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero


def count_substring(string, sub_string):
    """
    Cuenta cuantas veces aparece el sub_string
    en el string
    Args:
        string: (string)
        sub_string: (string)
    rerturn : int
    """

    return string.count(sub_string)



if __name__ == "__main__":
    main()
    string = "Hola Codo a Codo"  # input().strip()
    sub_string = "codo"  # input().strip()
    count = count_substring(string, sub_string)
    print(count)

    str = "este es un string que tiene varias coincidencias de strings con el sub-str"
    sub_str = "string"

    print("La palabra [", sub_str, "] aparece ", count_substring(str, sub_str), " veces")

 
    