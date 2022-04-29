import json


RUTA = "sem11/config.json"


def recuperarConfigJson():
	archivo = open(RUTA, "r") # r = read = modo solo lectura
	config = json.load(archivo)
	archivo.close()
	
	# print(type(contenido))
	# print(contenido)
	print(config["cadena_minusculas"])


def main():
	recuperarConfigJson()


if (__name__ == "__main__"):
	main()