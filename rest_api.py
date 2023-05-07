import requests


def check_status_code(status_code):
    if status_code != 200:
        raise Exception(f"Request failed with status code {status_code}")


# Task 1 get gifs links from GIFTY by word

# create correct request link and make request for GIFTY
def get_json_from_gifty(word: str):
    api_key = "D1c65XRNqoxmg3YSUcaXNy9FcTLYVFPx"
    resp = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={word}&limit=5")
    check_status_code(resp.status_code)
    return resp.json()


# processing and analyzing data
def get_gifty_links(word: str):
    try:
        data = get_json_from_gifty(word)
        for obj in data:
            print(f"{obj['title']} - {obj['url']}")
    except Exception as e:
        print("Founded an error:", e)


get_gifty_links("stand with ukraine")


# Task 2 get weather by location
# create correct request link and make request for getting current weather
def get_json_from_weathermap(api_key: str, coordinates: tuple):
    resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}"
                        f"&lon={coordinates[1]}&appid={api_key}")
    check_status_code(resp.status_code)
    return resp.json()


# create correct request link and make request for getting coordinates of city by its name
def get_city_coordinate(api_key: str, city_name: str):
    resp = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}")
    check_status_code(resp.status_code)
    return resp.json()


def get_weather(city_name: str):
    try:
        api_key = "9a99caca0eb10bc60aeb3d1a70fd478d"
        data = get_city_coordinate(api_key, city_name)
        data_meteo = get_json_from_weathermap(api_key, (data[0]["lat"], data[0]["lon"]))

        curr_temp = round(float((data_meteo['main']['temp'])) - 273.15, 1)  # Kelvin to Celsius
        feels_like_temp = round(float(data_meteo['main']['feels_like']) - 273.15, 1)  # Kelvin to Celsius

        print(f"City: {city_name}\n"
              f"Temperature: {curr_temp} C, "
              f"feels like {feels_like_temp} C. \n"
              f"Wind: {data_meteo['wind']['speed']} m/sec\n"
              f"{data_meteo['weather'][0]['main']}")

    except Exception as e:
        print("Founded an error:", e)


get_weather("Kyiv")


# Task 3 Get astronauts info
def get_astronaut():
    try:
        resp = requests.get("http://api.open-notify.org/astros.json")
        check_status_code(resp.status_code)
        data = resp.json()

        i = 1
        for person in data["people"]:
            print(f"Astronaut {i}: {person['name']}")
            i += 1
    except Exception as e:
        print("Founded an error:", e)


get_astronaut()
