"""
Dadas las variables: product_name y quantity, complete la función
is_product_available con el siguiente objetivo:
Buscar en un pandas DataFrame y devolver True si existe stock, False caso
contrario.
"""

import pandas as pd


_PRODUCT_DF = pd.DataFrame(
    {
        "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"], 
        "quantity": [3,10,0,5]
    }
)


def is_product_available(product_name, quantity):

    result = _PRODUCT_DF[_PRODUCT_DF['product_name'] == product_name]

    if not result.empty:

        if result['quantity'].item() >= quantity:
            return True
        else:
            print('Not enough stock')
            return False

    else:
        print('We do not have the requested flavor')
        return False


"""
2.2 Una opcion para resolver el loop infinito es darle al usuario unicamente una lista de productos
existentes con stock para que seleccione.
"""

def is_product_available_v2(product_name, quantity):

    result = _PRODUCT_DF[_PRODUCT_DF['product_name'] == product_name]
    response = False

    if not result.empty:

        if result['quantity'].item() >= quantity:
            response = True
        else:
            print('Not enough stock')
            response = False

    else:
        print('We do not have the requested flavor')
        response = False

    if not response:
        result = _PRODUCT_DF[_PRODUCT_DF['quantity'] > 0]
        print(result)

    return response