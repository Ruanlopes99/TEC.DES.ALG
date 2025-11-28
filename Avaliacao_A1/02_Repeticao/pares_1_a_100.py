print("--- Numeros Pares usando FOR ---")
# O range vai de 1 ate 100 (o 101 e exclusivo)
for numero in range(1, 101):
    # Se o resto da divisao por 2 for zero, e par
    if numero % 2 == 0:
        print(numero)

print("\n--- Numeros Pares usando WHILE ---")
contador = 1
while contador <= 100:
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1