import random
numero_magico = random.randint(1,10)
print(numero_magico)
entrada_usuario = int(input("Adivina el numero magico\n"))
if numero_magico != entrada_usuario:
    print(f"Perdiste, el número magico es {numero_magico}")

else:
    print("Has ganado la loteria")