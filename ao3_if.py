# controle de fluxo "if"

habilitado = False
if habilitado:
    print("esta habilitado!")

print("Esta linha sempre será impressa")

if habilitado:
    print("ok. Habilitado")
else:
    print("Nada feito. Não está habilitado")

media = 7
if media >= 6:
    print("aprovado")
elif media >= 5:
    print("recuperação")
elif media >=4:
    print("trabalho de recuperação")
else:
    print("reprovado")

print("terminado")

