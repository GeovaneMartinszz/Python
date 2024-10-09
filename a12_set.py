#Set (Conjunto)
# conjunto1 = {1,2,3,4,5,6,5,4}
# set não considera as repetiçoes

conjunto = {1,2,3,4,5,6,7,5,4}
print(conjunto)

nomes = {"Abigail", "Karl", "Gustavo", "Karl", "Abigail"}
print(nomes)

conjunto.add(9)
conjunto.remove(3)
print(conjunto)

outroconjunto = {7,5,3,9,1}
uniao = conjunto.union(outroconjunto)
print()
print(uniao)

diferença= conjunto.difference(outroconjunto)
print(diferença)

intersecçao = conjunto.intersection(outroconjunto)
print(intersecçao)