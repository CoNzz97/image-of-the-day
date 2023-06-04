import requests
import os
import dotenv

dotenv.load_dotenv("B:/Coding/Python/EnviromentVariables/.env") # Load .env file

NASA_API = os.getenv("aiod_nasa_open_api_key") # Load API key