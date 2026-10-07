import requests
import pandas as pd

url = "https://www.themealdb.com/api/json/v1/1/search.php?s=chicken"

response = requests.get(url)

data = response.json()

meals = data["meals"]

df = pd.DataFrame(meals)

print(df[["strMeal", "strCategory", "strArea"]])