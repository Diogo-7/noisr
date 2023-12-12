N = int(input("Baralho 1: "))
listan = [int(x) for x in input().split()]
M = int(input("Baralho 2: "))
listam = [int(x) for x in input().split()]
npar = 0
nimp = 0
for x in listan:
    for y in listam:
        if ((y+x)%2 != 0):
            nimp += 1
        else:
            npar += 1
print(str(npar)+" "+str(nimp))