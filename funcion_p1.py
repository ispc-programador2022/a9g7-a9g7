num1=int(input("Ingrese el número a sumar"))
num2=int(input("Ingrese el siguiente número a sumar"))
num3=int(input("Ingrese el número a sumar por los dos anteriores"))

def suma (x, y):
    return x + y

print("La suma de los números es: ",suma(num1, num2) + num3)