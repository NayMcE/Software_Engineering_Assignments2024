# create a console app using trivia API where users can select difficulty and types of questions they would like to answer.
# score the answers they make and using return function print in console.
# while users are on a winning streak print feedback to console. If users are struggling make suggestions.
#
# string slicing is needed

import requests

endpoint = "https://opentdb.com/api.php?amount=50"
response = requests.get(endpoint)
print("response is:", response)
data = response.json()
#print(data)


#create a welcome message from the Knowledge Tester console app.
print("Welcome! I'm your friendly Knowledge Tester")
print("Let's begin today by choosing a level!")

#create a variable with the input for user to enter level of difficulty for the quiz
level = input("Would you like your quiz to be easy, medium or hard?")
#create conditionals for feedback depending on the user input and use query string parameters to choose set of questions.
if level == "easy":
    endpoint = "https://opentdb.com/api.php?amount=20&difficulty=easy"
    print("OK great, let's keep it easy for today!")
elif level == "medium":
    endpoint = "https://opentdb.com/api.php?amount=20&difficulty=medium"
    print("Sounds good. Let's spice things up a bit!")
elif level == "hard":
    endpoint = "https://opentdb.com/api.php?amount=20&difficulty=hard"
    print("I like your style, you must be a knowledge wizz!")
else:
    print("You need to choose a level!")
# get level input from user and create a new function that selects all questions with requested level.

for question in data["results"]:
    print(question["question"])
