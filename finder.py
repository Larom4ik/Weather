import requests

# ===================класс поиска погоды====================================
class WeatherFinder:
    def __init__(self):
        self.city = None

    def set_city(self, city):
        self.city = city

    def get_weather(self):
        name_city = self.city
        api_key = '9aa0109ac3d84c51a2d3a6559150d675'
        api_adress = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q='
        url = api_adress + name_city
        json_data = requests.get(url).json()
        # ====================выполнение запроса====================================
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        # ====================обработка пришедших данных====================================

        final_info = condition + "\n" + ' ' + str(temp) + "°"
        final_data = "\n" + "Максимальная температура: " + str(max_temp) + "\n" + "Минимальная температура: " + \
                     str(min_temp) + "\n" + "Давление:" + str(pressure) + "\n" + "Влажность: " + str(humidity) + \
                     "\n" + "Скорость ветра: " + str(wind) + "\n"
        # ====================настройка вывода данных====================================
        return final_info, final_data, condition
# ====================Выполнение и обработка запроса погоды====================================
