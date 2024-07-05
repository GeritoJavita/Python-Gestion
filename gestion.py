
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



#Clasficar los productos

def clasificar_productos(inventario):
    baratos = []
    moderados = []
    caros = []

    for producto, detalles in inventario.items():
        precio = detalles['precio']
        if precio < 200000:
            baratos.append(producto)
        elif 200000 <= precio <= 400000:
            moderados.append(producto)
        else:
            caros.append(producto)
     return baratos, moderados,caros
        


os.system("cls")
print(inventario)
baratos, moderados, caros = clasificar_productos(inventario)
print(f"Baratos: {baratos}")
print(f"Moderados: {moderados}")
print(f"Caros: {caros}")


