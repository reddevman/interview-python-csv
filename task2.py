"""
1. Crear nuevo csv con id de producto e id de cliente separado por espacios(product_customers.csv)
2. Servirá para ver los clientes que han comprado ese producto

Ejemplo visual:
id,customer_ids
0,1 3 0 4
"""
import pandas as pd

# Lectura de los csv
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv").set_index("id")
products = pd.read_csv("products.csv").set_index("id")

# Split para la creación de la lista sin espacios
orders.products = orders.products.str.split(" ").apply(
    lambda order_list: [int(item) for item in order_list]
)

products["customers"] = [set() for _ in range(len(products))]

for index, row in products.iterrows():
    for index2, row2 in orders.iterrows():
        if index in row2.products:
            row.customers.add(row2.customer)

products["customer_ids"] = products["customers"].apply(
    lambda x: ''.join(str(list(x)).split(",")).replace("[", "").replace("]", "")
)

products["customer_ids"].to_csv("product_customers.csv", index=True, header=True)
