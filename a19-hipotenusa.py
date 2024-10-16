# usando a biblioteca Math

from math import hypot 

cateto0oposto = float(input("Cateto oposto: "))
catetoAdjacente = float(input("Cateto adjacente: "))
hipotenusa = (cateto0oposto ** 2 + catetoAdjacente ** 2) ** 0.5

print(f"a hipotenusa mede {hipotenusa: .2f}")

hipo = hypot(cateto0oposto, catetoAdjacente)
print((f"usando hypot: {hipo: .0f}"))