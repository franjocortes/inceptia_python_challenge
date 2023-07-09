"""
Completar la función validate_discount_code con el siguiente objetivo:
- Dada la lista de códigos de descuento vigentes y un código de descuento
  mencionado por el cliente, devuelve True si la diferencia entre el código
  mencionado y los códigos vigentes es menor a tres caracteres, en al menos
  uno de los casos.
Por diferencia se entiende: caracteres que están presentes en el código brindado, pero
no en el código evaluado de la lista o viceversa.
"""


_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021",
"Navidad2x1", "heladoFrozen"]

_VALID_DIFF = 3


def compare_diff(word1, word2):

    if word1 is None or word2 is None:
        return []
    
    character_list = []

    def compare(value_1, value_2):

        for i in range(len(value_1)):
            char_1 = value_1[i]

            for j in range(len(value_2)):
                char_2 = value_2[j]

                if char_1 == char_2:
                    break
                else:
                    if j == len(value_2) - 1 and value_1[i] not in character_list:
                        character_list.append(value_1[i])

    compare(word1, word2)
    compare(word2, word1)

    return character_list


def validate_discount_code(discount_code):
    """
    Ejemplo:
    "primavera2021" deberia devolver True, ya que al compararlo:
    vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
    vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o', 'm', 'V', 'p', 'v')
    vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0', 'x', 'e', 'd', 'p', 'r')
    vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i', 'v', 'n', 'o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
    """

    for code in _AVAILABLE_DISCOUNT_CODES:
        output_list = compare_diff(discount_code, code)
        print('vs', code, output_list)
        if len(output_list) < _VALID_DIFF:
            return True
    return False