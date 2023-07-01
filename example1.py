import requests

# Replace 'your_api_key' with your actual Spoonacular API key
api_key = 'your_api_key'
url = 'https://api.spoonacular.com/recipes/complexSearch'

params = {
    'apiKey': api_key,
    'diet': 'vegetarian',
    'cuisine': 'Indian',
    'number': 5,
    'includeNutrition': True
}

response = requests.get(url, params=params)

if response.status_code == 200:
    recipes = response.json()['results']
    for recipe in recipes:
        print(f"Recipe ID: {recipe['id']}")
        print(f"Title: {recipe['title']}")
        print(f"Image: {recipe['image']}")
        print(f"URL: https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']}")
        print("\n")
else:
    print(f'Request failed with status code {response.status_code}')
