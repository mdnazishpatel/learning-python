# import requests

# def get_weather(latitude, longitude):
#     response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
#     data = response.json()
#     return data['current']['temperature_2m']

# # Get temperature for different cities
# paris_temp = get_weather(48.85, 2.35)
# london_temp = get_weather(51.50, -0.12)
# tokyo_temp = get_weather(35.68, 139.69)
# india_temp= get_weather(20.5937, 78.9629)

# print(f"Paris: {paris_temp}°C")
# print(f"London: {london_temp}°C")
# print(f"Tokyo: {tokyo_temp}°C")
# print(f"india:{india_temp}c")
import requests

def cooking():
    response = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s=chicken")
    data = response.json()
    return data 
data = cooking()
for meal in data["meals"]:
    print(f"Recipe: {meal['strMeal']}")
    print(f"Category: {meal['strCategory']}")
    print(f"Cuisine: {meal['strArea']}")
    print("--------------------")
