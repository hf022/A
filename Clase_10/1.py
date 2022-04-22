














def guardar_cadena (cadena):
    archivo = open ("Clase_10/cadena_formateada.txt" , "w")
    archivo.write (cadena)
    archivo.close()
    print ("Se ha guardado la cadena en el archivo ")


    pass


# Flujo principal
if (__name__ == "__main__"):
	apellido = "Pompin"
	nombre = "Pepe"
	edad = 40
	saldo = 15480.815

cadena_formateada = f"Cadena de ejemplo: {apellido.upper()}, {nombre}, edad: {edad}, saldo: $ {saldo:.2f} AR"
    
guardar_cadena (cadena_formateada)
