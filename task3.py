"""
1. id de los clientes
2. Nombre
3. Apellidos
4. Euros totales gastados en todas las compras que haya hecho
5. Generar archivo customer_ranking.csv 
"""

import pandas as pd

# Lectura de los csv
orders = pd.read_csv("orders.csv").set_index("id")
customers = pd.read_csv("customers.csv").set_index("id")
products = pd.read_csv("products.csv").set_index("id")

orders.products = orders.products.str.split(" ").apply(
    lambda order_list: [int(item) for item in order_list]
)

orders["prices"] = orders.products.apply(lambda x: [products.loc[v].cost for v in x])

# Para cada registro realiza la suma total
orders["total_euros"] = orders["prices"].apply(lambda suma: sum(suma))

# Agrupa el DataFrame por cliente con la función suma
nuevo_df = orders.groupby(["customer"]).sum()

#pd.concat([nuevo_df, customers], axis=1)
# Unir el DataFrame antes creado con los clientes
dfJoin = nuevo_df.join(customers)

# Establece como índice el id
dfJoin.index.names = ['id']

#df.columns = ['a', 'b']

# Generación del csv con la columna total_euros en orden descendente
dfJoin[["firstname", "lastname", "total_euros"]].sort_values(
    by=["total_euros"], ascending=False
).to_csv("task3_customer_ranking.csv", index=True, header=True)
