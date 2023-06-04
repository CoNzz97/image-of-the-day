import requests
import os
import dotenv

dotenv.load_dotenv("B:/Coding/Python/EnviromentVariables/.env") # Load .env file
APOD_URL = "https://api.nasa.gov/planetary/apod"
NASA_API = os.getenv("aiod_nasa_open_api_key") # Load API key
params = {
    "api_key": NASA_API,
}

with requests.get(APOD_URL, params) as request:
    request.raise_for_status()
    returned = request.json()

image_of_the_day = returned["url"]
image_title = returned["title"]
image_explanation = returned["explanation"]

print(image_explanation)
