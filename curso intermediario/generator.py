import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(100)]
generator = (n for n in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)
print()
print()

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=10)
for n in gen:
    print(n)