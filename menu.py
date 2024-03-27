from suma import suma

if __name__ == "__main__":
    print("1. Suma")
    print("2. Fin")
    opcion = int(input("Ingrese opcion: "))
    if opcion == 1:
        valor1 = int(input("Ingrese valor 1"))
        valor2 = int(input("Ingrese valor 2"))
        print(suma(valor1, valor2))
        