'''def calc(v1, v2):
    return v1 * v2


print(calc(2, 2))


l = lambda v3, v4: v3 * v4

print(l(2, 5))'''

lista = [
    ['p1', 10],
    ['p2', 6],
    ['p3', 15],
    ['p4', 4],
    ['p5', 9],
]


lista.sort(key=lambda item: item[1], reverse=True)
for i in lista:
    print(i)
