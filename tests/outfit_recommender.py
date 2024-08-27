import json

def load_outfits():
    with open('tests/outfit_options.json','r') as file:
        return json.load(file)

def recommend_outfit(temp,weather_desc):
    outfits=load_outfits()

    if temp < 10:
        return outfits['cold']
    elif 10<=temp<=20:
        return outfits['cool']
    elif 20<=temp<=30:
        return outfits['warm']
    else:
        return outfits['hot']