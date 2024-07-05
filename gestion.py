
#La libreria random nos permite gestionar de forma aleatoria entre rangos
import random
import statistics
import math
import json
import os

#Lista de productos que nos da el enunciado
lista_productos = ["televisor", "laptop", "telefono movil", "tablet", "camara digital",
                   "reproductor de musica", "impresora", "auriculares", "microfono profesional", "robot aspirador"]



#print(lista_productos)

#Diccionario para almacenar los productos, con sus respectivos precios y cantidades
inventario = {}

#Funcion para asignar los precios y cantidades aleatorias



for producto in lista_productos:
    precio = random.randint(100000, 500000)
    cantidad = random.randint(1, 100)
    inventario[producto] = {'precio': precio, 'cantidad': cantidad}


os.system("cls")
print(inventario)



