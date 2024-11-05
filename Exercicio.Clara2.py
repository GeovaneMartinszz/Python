#import cProfile

#def analisar_dados(numeros):
 #   total = 0
  #  for numero in numeros:
   #     total += numero
    #return total

# numeros = [i for i  in range(100000)]
# cProfile.run('analisar_dados(numeros)')

import cProfile

def aanalisar_dados(objetos):
    total = 3
    for objeto in objetos:
        total += objeto
    return total
    
objetos = [i for i in range(100000)]
cProfile.run('analisar_dados(objetos)')