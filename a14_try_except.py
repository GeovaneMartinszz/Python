# Usando TRY ... EXCEPT

def dividir(a , b):
    if b != 0:
        quociente = a / b
        print(f"{a} dividido por {b} é {quociente}")
    else:
        print(f"Impossivel dividir por 0 (zero!")

a = int(input("SEM TRY - digite o dividendo: "))
b = int(input("SEM TRY - digite o divisor: "))
dividir(a , b)

def dividircomtry():
    try:
        dividendo = int(input("COM TRY - digite o dividendo: "))
        divisor = int(input("COM TRY - digite o divisor: "))
        quociente = dividendo / divisor
        print(f"{dividendo} dividido por {divisor} é igual a {quociente}")
    except ValueError:
        print(f"ERRO!: voçê digitou um valor invalido")
    except ZeroDivisionError:
        print(f"Impossivel dividir por 0 (zero)!")
    else:
        print("Nenhum erro ocorreu")
    finally:
        print("Este bloco 'finally' sempre sera executado")

dividircomtry()            