import requests

response = requests.get("https://openmensa.org/api/v2/canteens/195/meals")
data = response.json()

for day in data:
    meals = day["meals"]
    for meal in meals:
        if meal["category"] != "Hauptgerichte": continue
        meal_name = meal["name"]
        print(meal_name)
