import requests


# Task 1 get gifs links from GIFTY by word

# create correct request link and make request for GIFTY
def get_json_from_gifty(word: str):
    api_key = "D1c65XRNqoxmg3YSUcaXNy9FcTLYVFPx"
    req = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={word}&limit=5")
    return req.json()


# processing and analyzing data
def print_json_data(data: list):
    status = int(data["meta"]["status"])
    match status:
        case 200:
            list_obj = data["data"]
            for obj in list_obj:
                print(f"{obj['title']} - {obj['url']}")
        case 401:
            print("User authentication problems. Check your api key")
        case _:
            print(f"There is some unexpected service answer: {data['meta']['msg']}")


def get_gifty_links(word: str):
    print_json_data(get_json_from_gifty(word))


get_gifty_links("stand with ukraine")


# Task 2 get weather by location
# create correct request link and make request for getting current weather
def get_json_from_weathermap(api_key: str, coordinates: tuple):
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}"
                       f"&lon={coordinates[1]}&appid={api_key}")
    return req.json()


# create correct request link and make request for getting coordinates of city by its name
def get_city_coordinate(api_key: str, city_name: str):
    req = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}")
    return req.json()


def get_weather(city_name: str):
    try:
        api_key = "9a99caca0eb10bc60aeb3d1a70fd478d"

        data = get_city_coordinate(api_key, city_name)
        if type(data) is dict:
            raise Exception(f"Cod {data['cod']}. {data['message']}")
        data_meteo = get_json_from_weathermap(api_key, (data[0]["lat"], data[0]["lon"]))

        cod = int(data_meteo['cod'])
        if cod != 200:
            raise Exception(f"Cod {data_meteo['cod']}. {data_meteo['message']}")

        curr_temp = round(float((data_meteo['main']['temp'])) - 273.15, 1)  # Kelvin to Celsius
        feels_like_temp = round(float(data_meteo['main']['feels_like']) - 273.15, 1)  # Kelvin to Celsius
        print(f"City: {city_name}\nTemperature: {curr_temp} C, feels like {feels_like_temp} C. \n"
              f"Wind: {data_meteo['wind']['speed']} m/sec\n{data_meteo['weather'][0]['main']}")

    except Exception as e:
        print("Founded an error:", e)


get_weather("Kyiv")

# Task 3 Get astronauts info
def get_astronaut():
    req = requests.get("http://api.open-notify.org/astros.json")
    data = req.json()

    i = 1
    for person in data["people"]:
        print(f"Astronaut {i}: {person['name']}")
        i += 1


get_astronaut()
