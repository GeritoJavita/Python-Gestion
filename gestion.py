
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



#Clasficar los productos por orden de precios, de los mas baratos a los mas caros

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
    return baratos, moderados, caros



# Funcion para ver las con los requisitos obligatorios mencionados

def ver_estadisticas(inventario):
    producto_mas_caro = max(inventario, key=lambda x: inventario[x]['precio'])
    producto_mas_barato = min(inventario, key=lambda x: inventario[x]['precio'])
    promedio_precios = sum(item['precio'] for item in inventario.values()) / len(inventario)
    geometrica_cantidades = math.exp(sum(math.log(item['cantidad']) for item in inventario.values()) / len(inventario))
    valor_total_inventario = sum(item['precio'] * item['cantidad'] for item in inventario.values())
    
    print(f"Producto más caro: {producto_mas_caro} ({inventario[producto_mas_caro]['precio']} CLP)")
    print(f"Producto más barato: {producto_mas_barato} ({inventario[producto_mas_barato]['precio']} CLP)")
    print(f"Promedio de precios: {promedio_precios} CLP")
    print(f"Media geométrica de las cantidades: {geometrica_cantidades}")
    print(f"Valor total del inventario: {valor_total_inventario} CLP")





baratos, moderados, caros = clasificar_productos(inventario)
ver_estadisticas(inventario)
print(f"Baratos: {baratos}")
print(f"Moderados: {moderados}")
print(f"Caros: {caros}")


