'''def soma(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


soma1_2_3 = soma(1, 2, 3)
print(soma1_2_3)
numeros = soma(5,7)
print(numeros)'''

def parimpar(num):
    if num % 2 == 0:
        print("par")
    else:
        print("impar")
    return num
num = parimpar(2)
num = parimpar(3)
num = parimpar(10)

