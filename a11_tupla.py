# TUPLA
# tupla = (elemento1, elemento2, ...)

variavel1 = 9 # variavel numerica
variavel2 = "texto" # variavel tipo string
variavel3 = True # variavel do tipo boleano
variavel4 = ["item1", "item2", "item3"] # lista
variavel5 = ("item1", "item2", "...") # tupla
variavel6 = {1,2,3,4, ...} # set ou conjunto

tupla = (1, "olá", 3.14, True, 'c') # é imutavel
tuplaDireta = 0, "Edson", 1,618, 'p', "Edson"
tuplavazia = ()
tuplasimples = (27,)

print(tupla[1])
print(tupla[3])

print()
for indice, elemento in enumerate(tupla):
    print(f"{indice}: {elemento}")

tuplaninhada = ((1,2,3) , 1, True, [1,4, "sim"])
print(tuplaninhada[0])
print(tuplaninhada[1])
print(tuplaninhada[3][2])

print(len(tuplaDireta))
print(tupla.index(3.14))
print(tuplaDireta.count("Edson"))

string = "Curso de Python"
print(tuple(string))

novaTupla = tuple(string)
