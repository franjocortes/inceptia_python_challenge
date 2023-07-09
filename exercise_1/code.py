"""
Completar el método is_hot_in_pehuajo con el siguiente objetivo:
Consultar la información de clima y devolver True si la temperatura actual
supera los 28 grados celsius o False caso contrario. Esto implica incluso
devolver False ante cualquier excepción http.

API Información de clima:
Link a documentacion: https://openweathermap.org/current#geo
"""
import requests

_TEMP_REF = 28.00 

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        units = 'metric'
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&units={units}&appid={cls.API_KEY}'

        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            return False
        data = response.json()
        temp_value = data['main']['temp']

        return True if temp_value > _TEMP_REF else False
