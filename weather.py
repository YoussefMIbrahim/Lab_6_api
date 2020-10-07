import requests
from pprint import pprint
import os
from datetime import datetime


key = os.environ.get('WEATHER_KEY')


def main():

    country = input('enter the name of the country code: ').strip().lower()
    city = input('Enter the name of the city: ').strip().lower()

    country_city = city +','+country

    
    data = make_request(country_city)

    if data != None:

        forecast_list = data['list']

        pprint(data)
        for f in forecast_list:
            time = f['dt']
            date = datetime.fromtimestamp(time)
            temp = f['main']['temp']
            wind = f['wind']['speed']
            description = f['weather'][0]['description']
            print(f'At {date} Temperature: {temp}C wind speed: {wind} M/s, {description}  ')







def make_request(country):

    try:
        query = {'q' : country, 'units' : 'metric', 'appid' : key}
        url = 'http://api.openweathermap.org/data/2.5/forecast'

        res = requests.get(url, params=query)
        res.raise_for_status()

        data = res.json()

        return data


    except Exception as e:
        print(f'there was an error runnning this request: {e}')
        




if __name__ == "__main__":
    main()