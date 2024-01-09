import os

import requests


def obtenir_meteo_ville(ville):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": ville,
        "appid": os.environ["meteo_key"],
        "units": "metric",  # Vous pouvez changer 'metric' en 'imperial' pour les unités impériales
        "lang": "fr",
    }

    try:
        reponse = requests.get(base_url, params=params)
        print(reponse)
        print(reponse.url)
        donnees_meteo = reponse.json()

        if donnees_meteo["cod"] == "404":
            return f"La ville '{ville}' n'a pas été trouvée."
        else:
            temperature = donnees_meteo["main"]["temp"]
            description = donnees_meteo["weather"][0]["description"]
            return f"Météo actuelle à {ville}: Température {temperature}°C, Description: {description}"
    except Exception as e:
        return f"Une erreur s'est produite : {e}"
