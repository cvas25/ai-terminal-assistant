import requests

def get_joke():

    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)

    return response.json()