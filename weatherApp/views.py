from django.shortcuts import render
import requests

def get_weather_data(city_name):
    api_key = '266686c4d633ee17a8b1c352e1319d11'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    response = requests.get(base_url, params={'q': city_name, 'appid': api_key, 'units': 'metric'})
    return response.json()

def weather_home(request):
    city_name = request.GET.get('city', 'London')
    weather_data = get_weather_data(city_name)
    context = {
        'weather_data': weather_data,
        'city_name': city_name
    }
    return render(request, 'weatherApp/weather_home.html', context)
