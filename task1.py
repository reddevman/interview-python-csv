"""
1. Asociar id productos con su precio
2. Sumar el total de cada pedido
3. Crear nuevo csv con id de pedido y suma total de cada pedido (order_prices.csv)
"""
# Importación de la librerías pandas
import pandas as pd

# Lectura de los csv fijando como index el campo id
# De esta manera evitamos que pandas adjudique un id automáticamente
orders = pd.read_csv("orders.csv").set_index("id")
products = pd.read_csv("products.csv").set_index("id")

"""
- Declaración de nueva variable
- Convertir a lista mediante método split eliminando espacios
- apply() aplica la función lambda a todos los elementos
- Función lambda que convierte a entero todos los elementos de la lista iterándolos 
"""
orders.products = orders.products.str.split(" ").apply(
    lambda order_list: [int(item) for item in order_list]
)


""" 
- Declaración de nueva variable
- Para todos los elementos de la variable orders.products se le aplica la función lambda
- Función lambda que localiza en el csv de productos todos los cost y los itera
para almacenarlos en la nueva variable order['prices']
"""
orders["prices"] = orders.products.apply(lambda x: [products.loc[v].cost for v in x])

"""
- Declaración de nueva variable para crear la suma de todos los precios de los productos que tienen cada pedido
- Se aplica a todos los precios obtenidos
- Suma con la función específica sum() dentro de la lambda
"""
orders["SumaPedido"] = orders["prices"].apply(lambda suma: sum(suma))

# Creación del csv nuevo
orders[["SumaPedido"]].to_csv("order_prices.csv", index=True, header=True)


