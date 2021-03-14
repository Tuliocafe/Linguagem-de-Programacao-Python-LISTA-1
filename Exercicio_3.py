
numero = int(input("Qual valor para sequência de Fibonacci deseja: "))
ultimo = 1
penultimo = 1

if (numero == 1) or (numero == 2):
    print("1")
else:
    for count in range(2, numero):
        valor = ultimo + penultimo
        penultimo = ultimo
        ultimo = valor
        count += 1
    print(valor)
