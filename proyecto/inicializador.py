import json
import os

# acá se va almacenar el inventario
FILE_NAME = 'inventory.json'


def cargar_inventario():
    #Carga el inventario desde un archivo .JSON
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return {}


def guardar_inventario(inventario):
    #Guarda el inventario en un archivo JSON
    with open(FILE_NAME, 'w') as file:
        json.dump(inventario, file, indent=4)
