
"""
t_max = 320
t_min = 300

CTD_LECTURAS = 5
LECTURAS = (300, 320, 305, 301, 303)

acumulado = 0 
prmedio = 0 

for lectura in LECTURAS:
    acumulado = acumulado + lectura

promedio = acumulado / CTD_LECTURAS

print (promedio)




t_max = 320
t_min = 300

CTD_LECTURAS = 5
LECTURAS = random.int(300 , 320)

acumulado = 0 
prmedio = 0 

for lectura in LECTURAS:
    acumulado = acumulado + lectura

promedio = acumulado / CTD_LECTURAS

print (promedio)

"""

import random
t_inicial = 30
t_max = 320
t_min = 300
lecturas = 5



acumulado = 0 
promedio = 0 


for ciclo in range (lecturas):
    ciclo = random.randint (t_min, t_max)
    acumulado = acumulado + ciclo

    print (ciclo)

#print (acumulado)

promedio = acumulado / lecturas
print (promedio)




 
