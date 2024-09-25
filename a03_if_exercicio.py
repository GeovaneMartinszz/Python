# faça uma rotina com o uso de if, elif, else quer receba um valor numerico inteiro entre 1 e 100 e print se a pessoa com a idade obrigatoriamente vota, se vota compulsoriamente ou não pode votar

acordei = False
if acordei:
    print("acordei cedo")
else:
    print("faltei na escola") 

if acordei:
    print("me arrumei e fui ao colegio")
else:
    print("Não fui ao colegio e tomei esporro")

idade = int(input("Digite a idade: ")) 
if idade >= 60:
    print("voto opcional")
elif idade >= 18:
    print("o voto é obrigatorio")
elif idade >= 16:
    print("voto opcional")
else:
    print("Não e obrigado a votar")

if idade >= 60 or idade <=16 and idade >= 16:
    print("o voto é opcional")
elif idade >= 18:
    print("O voto é obrigatorio")
else:
    print("Não pode votar")