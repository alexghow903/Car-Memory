import json
import geocoder
from datetime import datetime


def create(text, file):
    g = geocoder.ip('me')
    date = str(datetime.now())

    dictionary = { text: {
        "Geolocation": {
            "Latitude": g.lat,
            "Longitude": g.lng
            },
        "Timestamp": date
        }
    }
    f = open("recognized.json", "w")
    file.update(dictionary)
    json.dump(file, f, indent=4)
    f.close()

def check(text):
    f = open("recognized.json", "r+")
    file = json.load(f)
    f.close()
    print(file.get(text))
    if file.get(text) == None:
        create(text, file)
    else:
        lat = file[text]["Geolocation"]["Latitude"]
        lng = file[text]["Geolocation"]["Longitude"]
        time = file[text]["Timestamp"]
        print(f"You saw {text} at {lat}, {lng} at {time}.")
        # swap out for call to app api.