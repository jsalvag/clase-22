
def main():
    """
    main() -> None
    """
    myVariable = complex()
    print(myVariable)
    sumatoria(3)
    print(calVolumenParalelepipedo(2,3,10))
    print(sumatoria(3))
    return None

def sumatoria(x):
    resultado = (x*(x+1))/2
    return resultado

def calVolumenParalelepipedo(x,y,z):
    resultado = x*y*z
    return resultado


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