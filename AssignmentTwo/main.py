import requests # import the trivia api endpoint url in the get_question_pool function
import html # import to remove the ascii characters from the question and answer text
import random # module used to randomly shuffle the answer choices for the user

# get a pool of trivia questions
def get_question_pool():
    url = f"https://opentdb.com/api.php?amount=5&category=11"
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]

# Shuffle the answer choices for question
def shuffle_choices(choices: list):
    random.shuffle(choices)
    return choices

# print answer choices in the console
def print_choices(choices: list):
    for choice_index, choice in enumerate(choices):
        print(f"{choice_index+1}. {html.unescape(choice)}")

# get the users choice in the console
def get_user_choice():
    while True:
        user_choice = int(input("Enter the number of your choice: "))
        if user_choice in range(1,5):
            return user_choice - 1
        else:
            print("Invalid input. Enter the number of your choice.")

# play the game
# get question key from the list "results"
def play_game():
    question_pool = get_question_pool()
    score = 0
    for question in question_pool:
        question_text = html.unescape(question["question"])
        print(question_text)
 # choices list from shuffle_choices requests keys
        choices = question["incorrect_answers"]
        choices.extend([question["correct_answer"]])
        shuffled_choices = shuffle_choices(choices)
        print_choices(shuffled_choices)
        user_choice_index = get_user_choice()
        user_choice_text = shuffled_choices[user_choice_index]
        correct_choice_text = html.unescape(question["correct_answer"])
        if user_choice_text == correct_choice_text:
            print(f"Correct! You answered: {correct_choice_text}\n")
            score += 1
            print(f"You're score is: {score}\n")
        else:
            print(f"Incorrect. The correct answer is: {correct_choice_text}\n")
    # retrieve the final score and print to console as well as write to txt file
    final_score = score
    print(f"You're final score is : {final_score}")
    with open("C:\\Users\\naomi\\PycharmProjects\\CFG-Assignments\\AssignmentTwo\\final_score.txt", "w") as file:
        file.write(f"You're final score is: {final_score}")
    return score


#call the function
play_game()

