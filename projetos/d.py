lista = input().split()
N = int(lista[0])
K = int(lista[1])
i = 0
resp = 0
while i < N:
    espaço = ""
    l = 0
    while l < K:
        espaço += "."
        l += 1
    floresta = str(input())
    if floresta.find(espaço) != -1:
        resp = 1
    i += 1
print(resp)