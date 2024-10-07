# função (de)

def hello():
    print("olá, mundo!")

def mensagem(msg):
    return f"mensagem: {msg}"

def multiplicar(x, y):
    return x * y

hello()
print(mensagem("cambio!!!"))
print(multiplicar(3, 12))

def saudacao(nome, cumpr="Olá"):
    print(f"{cumpr},{nome}")

saudacao("Geovane")
saudacao("Parissoto", "Bom dia")