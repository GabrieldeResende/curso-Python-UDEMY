def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma1_2_3 = soma(1, 2, 3)
print(soma1_2_3)
numeros = soma(10, 20, 60, 50)
print(numeros)
