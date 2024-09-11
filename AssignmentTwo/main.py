# create a console app using trivia API where users can select difficulty and types of questions they would like to answer.
# score the answers they make and using return function print in console.
# while users are on a winning streak print feedback to console. If users are struggling make suggestions.
#
# string slicing is needed

import requests

#create a welcome message from the Knowledge Tester console app.
print("Welcome! I'm your friendly Knowledge Tester")
print("Let's begin today by choosing a level!")

#create a variable with the input for user to enter level of difficulty for the quiz
level = input("Would you like your quiz to be easy, medium or hard?")
#create conditionals for feedback depending on the user input and use query string parameters to choose set of questions.
if level == "easy":
    endpoint = "https://opentdb.com/api.php?amount=5&difficulty=easy"
    response = requests.get(endpoint)
    data = response.json()
    print("OK great, let's keep it easy for today!")
    print(f"Endpoint is: {endpoint}")
elif level == "medium":
    endpoint = "https://opentdb.com/api.php?amount=5&difficulty=medium"
    response = requests.get(endpoint)
    data = response.json()
    print("Sounds good. Let's spice things up a bit!")
    print(f"Endpoint is:{endpoint}")
elif level == "hard":
    endpoint = "https://opentdb.com/api.php?amount=5&difficulty=hard"
    response = requests.get(endpoint)
    data = response.json()
    print("I like your style, you must be a knowledge wizz!")
    print(f"Endpoint is:{endpoint}")
else:
    print("You need to choose a level!")








