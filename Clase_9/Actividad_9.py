"""Como siempre, LEER atentamente el enunciado y tratar de fragmentar las distintas etapas lógicas. 
No importa si no se llegan a completar todos los puntos, pero por supuesto, intentar hacer la mayor 
cantidad posible:

Una persona trabaja como delivery en una pizzería de viernes a domingo. Percibe $ 300 por entrega los 
viernes y sábados, y $ 200 los domingos. Si suma al menos 20 entregas en la semana, obtiene un incentivo 
extra de $ 1000. Desea disponer de un resumen rápido por día y semana.

Etapas a realizar:

    Solicitar por consola el ingreso del número de entregas realizadas día x día.
    Mostrar un resumen de esas entregas y un subtotal de lo cobrado día x día.
    Mostrar el total de entregas y lo ganado en toda la semana (sumando el premio si corresponde).

Consignas a respetar:

    Utilizar al menos una lista, una tupla y una función.
    Utilizar el control if (__name__ == "__main__") para iniciar el flujo principal de código.

Recordar:

    Las tuplas son inmutables, no se puede modificar su contenido, por ende se aplican a elementos que no 
    necesitan ser cambiados durante la ejecución de código (constantes para cálculos, nombres de días, meses, etc).
    Se puede generar una lista vacía y luego ir agregando elementos a ella mediante el método append.

------------------------------------------


vier_y_sab = 300
domingo = 200
incentivo = 1000


vier = int(input("Ingresar cantidad de entregas los viernes: "))
sab = int(input("Ingresar cantidad de entregas los sábados: "))
dom = int(input("Ingresar cantidad de entregas los domingos: "))


subtotal_viernes = vier * vier_y_sab
subtotal_sabado = sab * vier_y_sab
subtotal_domingo = dom * domingo
total = subtotal_viernes + subtotal_sabado + subtotal_domingo

premio = vier + sab + dom

print (".........................................")

print ("Facturación día viernes: " , subtotal_viernes)
print ("Facturación día sábado: " , subtotal_sabado)
print ("Facturación día viernes: " , subtotal_domingo)

print (".........................................")

if ( premio > 20 ):
    print ("TOTAL FACTURADO: " , total + incentivo)
              
else:
    print ("TOTAL FACTURADO + INCENTIVO: " , total )

print (".........................................")


print ("_________________________")
print ()

----------------------------------

def cant ():
    cant = ""
    for c in range(3):
     int(input("Ingresar cantidad de entregas: "))
    


salida = f"{dias[indice]} = {subtotal_entregas} entregas"



    dat = {
        "dia": dias[c1],
        "entregas": cant,
    }

    print(dat)

"""



val_v = 300
val_s = 300
val_d = 200
incentivo = 1000

v = int(input("Ingresar cantidad entregas: "))
s = int(input("Ingresar cantidad entregas: "))
d = int(input("Ingresar cantidad entregas: "))

st_vie = v * val_v
st_sab = s * val_s
st_dom = d * val_d

total = st_vie + st_sab + st_dom

t_entregas = v + s + d

premio = total + 1000

entregas = (v, s, d,)

dias = ("Viernes", "Sabado", "Domingo")

st = (st_vie , st_sab , st_dom)


print ("......................")

print ("Cantidad de entregas:")

for c1 in range(3):
    
    salida = f"{dias[c1]} = {entregas[c1]}"

    print (salida)

print ("......................")

print ("Subtotal:")

for c2 in range(3):

    salida2 = f"{dias[c2]} = $ {st[c2]}"
 

    print (salida2)

print ("......................")


if ( t_entregas > 20 ):
    print ("TOTAL FACTURADO + INCENTIVO: $", total + incentivo)
              
else:
    print ("TOTAL FACTURADO: $",total )





