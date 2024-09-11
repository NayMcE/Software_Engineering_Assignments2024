from random import shuffle
import requests
import html
import random

#create a welcome message from the Knowledge Tester console app.
print("Welcome! I'm your friendly Knowledge Tester")
# print("Let's begin today by choosing a level!")

# def user_level():
#     level = input("Would you like your quiz to be easy, medium or hard? ")
#
# #create conditionals for feedback depending on the user input and use query string parameters to choose set of questions.
#     if level == "easy":
#         endpoint = "https://opentdb.com/api.php?amount=5&difficulty=easy"
#         response = requests.get(endpoint)
#         data = response.json()
#         print("OK great, let's keep it easy for today!")
#         print(f"Endpoint is: {endpoint}")
#     elif level == "medium":
#         endpoint = "https://opentdb.com/api.php?amount=5&difficulty=medium"
#         response = requests.get(endpoint)
#         data = response.json()
#         print("Sounds good. Let's spice things up a bit!")
#         print(f"Endpoint is:{endpoint}")
#     elif level == "hard":
#         endpoint = "https://opentdb.com/api.php?amount=5&difficulty=hard"
#         response = requests.get(endpoint)
#         data = response.json()
#         print("I like your style, you must be a knowledge whizz!")
#         print(f"Endpoint is:{endpoint}")
#     else:
#         print("You need to choose a level!")
#
# if __name__ == "__main__":
#     user_level()
#     get_questions()

endpoint = "https://opentdb.com/api.php?amount=10"
response = requests.get(endpoint)
data = response.json()["results"]

def get_categories():
    url = endpoint
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print(f"Could not retrieve data [{response.status_code}]")


def category_choice():
    for categories in data:
        print(html.unescape (categories["category"]))

category_choice()


user_category = input ("Which category would you like to choose?")


category_data = get_categories(user_category.lower())

for category in category_data["category"]:
    print(category["category]"])



