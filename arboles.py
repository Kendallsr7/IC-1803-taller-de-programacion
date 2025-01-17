valor = 0
izq = 1
der = 2


def crear_nodo(dato):
    return [dato, [], []]


def insertar(arbol, dato):
    if arbol == []:
        return crear_nodo(dato)
    if dato < arbol[valor]:
        arbol[izq] = insertar(arbol[izq], dato)
    else:
        arbol[der] = insertar(arbol[der], dato)
    return arbol


def buscar(arbol, dato):
    if arbol == []:
        return False
    if arbol[valor] == dato:
        return True
    if dato < arbol[valor]:
        return buscar(arbol[izq], dato)
    return buscar(arbol[der], dato)


def eliminar(arbol, dato):
    if arbol == []:
        return []
    if arbol[valor] == dato:
        if arbol[izq] == [] and arbol[der] == []:
            return []
        if arbol[izq] == []:
            return arbol[der]
        if arbol[der] == []:
            return arbol[izq]
        arbol[valor] = encontrar_menor(arbol[der])
        arbol[der] = eliminar(arbol[der], arbol[valor])
        return arbol
    if dato < arbol[valor]:
        arbol[izq] = eliminar(arbol[izq], dato)
    else:
        arbol[der] = eliminar(arbol[der], dato)
    return arbol


def encontrar_menor(arbol):
    if arbol[izq] == []:
        return arbol[valor]
    return encontrar_menor(arbol[izq])


arbol = []
arbol = insertar(arbol, 5)
arbol = insertar(arbol, 3)
arbol = insertar(arbol, 7)
arbol = insertar(arbol, 2)
arbol = insertar(arbol, 4)

print(arbol)
# [5, [3, [2, [], []], [4, [], []]], [7, [], []]]
#      5
#     / \
#    3   7
#   / \
#  2   4

arbol = eliminar(arbol, 3)
print(arbol)
# [5, [4, [2, [], []], []], [7, [], []]]
#      5
#     / \
#    4   7
#   /
#  2

arbol = insertar(arbol, 6)
arbol = insertar(arbol, 8)

print(arbol)
# [5, [4, [2, [], []], []], [7, [6, [], []], [8, [], []]]]
#      5
#     / \
#    4   7
#   /   / \
#  2   6   8

arbol = eliminar(arbol, 5)
print(arbol)
# [6, [4, [2, [], []], []], [7, [], [8, [], []]]]
#      6
#     / \
#    4   7
#   /     \
#  2       8


def altura(arbol):
    if arbol == []:
        return 0
    return 1 + max(altura(arbol[izq]), altura(arbol[der]))

print(altura(arbol))  # 3