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

    radioVariable = input("Ingrese el valor del radio: ")
    # terminar el chequeo y si no es float hacer algo...

    circunferencia = calcularCircunferencia(float(radioVariable))

    print(f"El valor de la circunferencia es: {circunferencia}" )

    return None

# Esto sera una constante
complex_zero = {0,0}

def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    

if __name__ == "__main__":
    main()