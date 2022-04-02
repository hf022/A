


""""

La tarea consiste en diseñar un algoritmo para controlar la temperatura de un horno de forma básica, 
leyendo valores desde un sensor y activando o desactivando 2 quemadores para aumentar o disminuir según 
se necesite.

Como no se dispone físicamente de los elementos, las lecturas se deben simular completando una matriz 
(lista) con valores al azar, usando el método randint de la librería random. Cuando sea necesario 
encender o apagar los quemadores, bastará con mostrar un print() con el mensaje en cuestión.

Etapas:

  1.  Ingresar una temperatura de prueba desde consola, mediante input, se usará para testear el algoritmo. 
      No olvidar la conversión a entero (int). Si se ingresa 0, finaliza la ejecución de código.

  2.  Usando el comando random.randint(min, max), generar una lista de 50 lecturas, min será 300 y max 320 grados.

  3.  Obtener la lectura promedio de la lista.

  4.  
  Comparar esta lectura promedio con la temperatura del punto 1. 

  Si la diferencia es mayor a 100 grados por debajo, se deben encender 2 quemadores; 
  Si es menor a 100, solo 1
  Si está por arriba del valor promedio, apagar siempre los 2. 
  En caso de estar dentro del rango correcto (300 a 320 grados), mostrar mensaje de horno a temperatura correcta.

   5. Retornar a ingresar una nueva temperatura objetivo.

En el ejercicio se podrán integrar distintos puntos vistos (uso de variables / constantes, condiciones, ciclos y matrices).


"""
import random

#t_inicial = 30
t_inicial = int(input("Ingresar temperatura inicial: "))
t_max = 320
t_min = 300
lecturas = 50
acumulado = 0 
promedio = 0 


print ("Valores: ")


for ciclo in range (lecturas):
    
    ciclo = random.randint (t_min, t_max)
    acumulado = acumulado + ciclo
    print (ciclo,"°C")
    

promedio = acumulado / lecturas
print ("Temperatura promedio:" , promedio ,"°C")

dt = promedio - t_inicial
print ("Δt:" , dt ,"°C")


#Si la diferencia es mayor a 100 grados por debajo, se deben encender 2 quemadores;
#Si es menor a 100, solo 1
#Si está por arriba del valor promedio, apagar siempre los 2. 
#En caso de estar dentro del rango correcto (300 a 320 grados), mostrar mensaje de horno a temperatura correcta.


if (dt < 100): 
    print ("Encendido quemador Nº1 y Nº2")

else:
    print ("Encendido quemador Nº1")

if (t_inicial > promedio): 
    print ("Apagado quemador Nº1 y Nº2")

if (promedio < t_max and promedio > t_min): 
    print ("Horno a temperatura correcta")










