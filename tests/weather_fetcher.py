from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
INPUT = input("Location ?")


def get_weather():
    params = {
        'q':INPUT,
        'appid':API_KEY,
        'units':'metric'
    }
    
    response = requests.get(BASE_URL, params = params)
    data = response.json()
    if response.status_code == 200:
        return data['main']['temp'], data['weather'][0]['description']
    else:
        raise Exception(f"Error Occured:{data['message']}")
    