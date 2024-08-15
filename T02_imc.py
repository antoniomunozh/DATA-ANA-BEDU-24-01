# Escribir un programa que calcule el IMC de una persona, el programa debe solicitar el peso y la altura (aka datos de entrada).
peso = int(input("¿Cuántos kilos pesas? "))
altura = float(input("¿Cuál es tu estatura en metros? "))

imc = round((peso / (altura **2)),2)
print(f"El indice de masa corporal de la persona es: {imc}")
