def funcao(n1):
    if ((n1%5==0) and (n1%3==0)):
        return "fizzbuzz"
    elif (n1 % 3 ==0):
        return "fizz"
    elif (n1 % 5 == 0):
        return "buzz"
    else:
        return n1

print(funcao(15))
print(funcao(3))
print(funcao(5))
print(funcao(7))