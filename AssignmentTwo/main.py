# create a console app using trivia API where users can select difficulty and types of questions they would like to answer.
# score the answers they make and using return function print in console.
# while users are on a winning streak print feedback to console. If users are struggling make suggestions.
#
# string slicing is needed

#create a welcome message from the Knowledge Tester console app.
print("Welcome! I'm your friendly Knowledge Tester")
print("Let's begin today by choosing a level!")

#create a variable with the input for user to enter level of difficulty for the quiz
level = input("Would you like your quiz to be easy, medium or difficult?")
#create conditionals for feedback depending on the user input.
if level == "easy":
    print("OK great, let's keep it easy for today!")
elif level == "medium":
    print("Sounds good. Let's spice things up a bit!")
else:
    print("I like your style, you must be a knowledge wizz!")

# get level input from user and create a new function that selects all questions with requested level.

def level_selection():
    if level == "easy":
        #retrieve easy question set
    elif level == "medium":
        #retrieve medium question set
    else:
        #retrieve difficult question set

#
