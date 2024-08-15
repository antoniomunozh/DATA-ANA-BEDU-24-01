# Escribir un programa que imprima la tabla de multiplicar de un numero que el usuario ingrese como dato de entrada.
tabla_del = int(input("Ingresa el número de la tabla que deseas imprimir: "))
for x in range(0,11):
    result = x * tabla_del
    print(f"{tabla_del} x {x} = {result}")







