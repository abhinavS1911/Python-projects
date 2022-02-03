import requests
from datetime import datetime as dt


API_KEY = "<API-KEY>"
APP_ID = "<APP-ID>"
END_POINT_NUTRIONX = "https://trackapi.nutritionix.com/v2/natural/exercise"
END_POINT_SHEETY = "https://api.sheety.co/2a8d82ed985426b651e4ec7d0003c270/workoutTracking/workouts"
USER_NAME = "<USERNAME>"
PASS_WORD = "<PASSWORD>"

HEADERS_NUTRIONX = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

query_input = input("Tell me which exercise you did today?:")
EXERCISE_PARAMETERS ={
 "query": f"{query_input}",
 "gender": "male",
 "weight_kg": 80.5,
 "height_cm": 186,
 "age": 20
}

# Data to be added in spreadsheet
today_date = str(dt.today().date()).split("-")
formatted_date = "/".join(reversed(today_date))
current_time = dt.today().time().strftime("%X")


response_nutrionx = requests.post(url=END_POINT_NUTRIONX, headers=HEADERS_NUTRIONX, json=EXERCISE_PARAMETERS)
nutrition_data = response_nutrionx.json()
# print(nutrition_data["exercises"])

bearer_headers = {
"Authorization": "Bearer <PASSWORD>"
}

for _ in nutrition_data["exercises"]:
    SHEETY_PARAMETERS = {
        "workout": {
            "date": formatted_date,
            "time": current_time,
            "exercise": _["name"].title(),
            "duration": _["duration_min"],
            "calories": _["nf_calories"]
        }
    }

    response_sheety = requests.post(url=END_POINT_SHEETY, json=SHEETY_PARAMETERS, headers=bearer_headers)
    print(response_sheety.status_code)



