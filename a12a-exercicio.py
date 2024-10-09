# Exercicios

# faça uma lista de 7 paises
# faço uma tupla com os mesmos paises
# faça um conjunto (set) com os mesmos paises
# Acrescente um pais na lista e no conjunto
# remova um pais da lista e do conjunto
# print os resultados

listapaises = ["Brasil", "Argentina", "Alemanaha", "Estados Unidos", "Grecia", "França", "Inglaterra"]
tupla = ("Brasil", "Argentina", "Alemanha", "Grecia", "Inglaterra", "Estados Unidos", "França")

conjuntoset = {"Brasil", "Argentina", "Alemanha", "Grecia", "Inglaterra", "Estados Unidos", "França", "Grecia", "Alemanha"}
conjuntoset.add("Colombia")
listapaises.append("Colombia")
print(conjuntoset)

conjuntoset.remove("Inglaterra")
listapaises.remove("Inglaterra")
print(conjuntoset)

print(listapaises)
print(tupla)
