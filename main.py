import json
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# .env file contains api keys in the format of API_KEY="xxxxxx", get it using os.environ['API_KEY']
load_dotenv()  # take environment variables from .env.

GENDER = "Male"
WEIGHT_KG = 105
HEIGHT_CM = 184
AGE = 54

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = os.environ['NUTRITIONIX_APP_ID']
NUTRITIONIX_APP_KEY = os.environ['NUTRITIONIX_APP_KEY']

nut_parameters = {
    "query": 'walked for 30 min',
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nut_parameters, headers=headers)
data = response.json()
print(data["exercises"][0])

Duration = data["exercises"][0]['duration_min']
Calories = data["exercises"][0]['nf_calories']
Exercise = data["exercises"][0]['name'].title()
Date = datetime.now().strftime("%d/%m/%Y")
Time = datetime.now().strftime("%H:%M:%S")

sheety_endpoint = "https://api.sheety.co/27e3609a0241b7d56179d12188a416ea/myWorkoutsCopy/workouts"

sheety_parmaters = { "workout": { "Date": Date, "Time": Time, "Exercise": Exercise, "Duration": Duration,"Calories": Calories} }
sheety_headers = { "Authorization" : "Bearer Dana5212" }


response2 = requests.post(url=sheety_endpoint, json=sheety_parmaters, headers=sheety_headers)
print(response2.text)