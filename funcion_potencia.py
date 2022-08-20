num1 = int(input("Ingrese el número a potenciar"))
num2 = int(input("Ingrese el número por el que lo va a elevar"))


def potencia(x, y):
    return x ** y


print("El resultado de la potencia es: ", int(potencia(num1, num2)))
