
from exercise_1.code import GeoAPI
from exercise_2.code import is_product_available, is_product_available_v2
from exercise_3.code import validate_discount_code


_OPTION_LIST_STR = """
1. Exercise 1 - GeoAPI
2. Exercise 2 - Is Product Available ?
3. Exercise 3 - Validate Discount Code
"""


def get_options():
    print(_OPTION_LIST_STR)
    option = input('Your choose (q for exit): ')

    try:
        return int(option)
    except ValueError:
        return False


if __name__ == '__main__':

    option = get_options()

    while option:

        if option == 1:
            print('GEO API')
            response = GeoAPI.is_hot_in_pehuajo()
            print(response)

        if option == 2:
            print('IS PRODUCT AVAILABLE ?')
            response = is_product_available('Granizado', 5)
            print(response)

            # test for 2.2 uncomment to test
            # response = is_product_available_v2('Frutilla', 2)
            # print(response)

        if option == 3:
            print('VALIDATE DISCOUNT CODE')
            response = validate_discount_code('verano021')
            print(response)
        
        else:
            print('Option invalid')

        option = get_options()

    print('Exit!!')


