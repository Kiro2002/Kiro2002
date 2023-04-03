A=["ola", "iza","ania", "jan", "damian" ]
B=["michał", "kamil", "damian"]
C=["asia", "iza", "piotr", "damian"]

zbior = set(A)
zbior2 = set(B)
zbior3 = set(C)

#Występuje w zbiorze A i B
print(zbior.intersection(zbior2))

#występuje w zbiorach A, B, i C
print(zbior.intersection(zbior2, zbior3))

# W zbiorze C ale nie ma w A
print (zbior3.difference(zbior))

# w zbiorze B ale nie ma w A i C
print(zbior2.difference(zbior, zbior3))

#przynajmniej 1 ze zbiorów----->chyba
print(zbior.symmetric_difference(zbior2))

#w zbiorze A ale nie ma ich w sumie zbioru B i C------->chyba
print(zbior.difference(zbior2.union(zbior3)))
