string = "hello world!"
for caracter in string:
    print(caracter)

print(string[6])
print(string[7:12])
print("Olá, mundo!"[5:10])
print("Bom dia!"[-1])

s1 = "Vamos"
s2 = "lá!"
print(s1 + " " + s2)
print(len("Tamanho de um texto."))
texto = len("Tamanho de um texto.")
print(texto)

mensagem = "Tudo que e solido se desmancha no ar."
print("lid" in mensagem) # True
print("y" in mensagem) # false

# fatiamento
slicing = mensagem[11:17]
print(slicing) # "é solido"

print(mensagem.upper())
print(mensagem.lower())
print(mensagem.replace("o ar", "a atmosfera"))
print(" Hoje em dia.  ".replace(" " , ""))
