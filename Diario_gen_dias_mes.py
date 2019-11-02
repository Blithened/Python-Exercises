"""

Un simple programa que me escribe automáticamente los días del mes, su día y un formato que manejo
para escribir mi diaro de manera más fácil

"""

import math

cue = input("mes par 31(y/n) feb(f): ")

dias = ['Lunes', 'Martes', 'Miércoles','Jueves', 'Viernes', 'Sábado',
        'Domingo']

dias.reverse()

nums = [x  for x in range(7)]
nums_letters = dict(zip(nums, dias))
print(nums_letters)
counter = int(input("En qué día termina el mes? (entrar numero dado arriba):  \n\t " )) 


if cue == 'y':
    

    for i in range (31, 0,-1):
        
        
        if counter == 7:   
            counter = 0
        print("%i. %s X ()" %(i,dias[counter]))

        counter = counter+1
if cue == 'n':

    for i in range (30, 0,-1):
        if counter == 7:
            
            counter = 0
        print("%i. %s X ()" %(i,dias[counter]))
        counter = counter+1
if cue == 'f':

    for i in range (28, 0, -1):
        if counter == 7:
            
            counter = 0
        print("%i. %s X ()" %(i,dias[counter]))
        counter = counter+1
