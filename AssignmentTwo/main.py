import requests # import the trivia api endpoint url in the get_question_pool function
import html # import to remove the ascii characters from the question and answer text
import random # module used to randomly shuffle the answer choices for the user


# get a pool of trivia questions from the trivia API
def get_question_pool(amount=5, difficulty="easy"):
    url = f"https://opentdb.com/api.php?amount={amount}&category=9&difficulty={difficulty}"
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
print("Hello and welcome to your friendly General Knowledge Tester! Come back each day and see if you can get a higher score!\n"
      "Your results will also be saved to an external file for you to review your answers and see where you went wrong! \n"
      "Save the file for future reference and keep practicing! You'll be a general knowledge master in no time!")
input("Press enter to start playing!\n")
# get question key from the list "results"
def play_game():
    question_number = int(input("How many questions would you like to answer? "))
    question_difficulty = input("What level would you like to choose: Easy, medium or hard? ").lower()
    question_pool = get_question_pool(amount = question_number,difficulty = question_difficulty )
    score = 0
    results = []
    for question in question_pool:
        question_text = html.unescape(question["question"])
        print(question_text)
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
            correct = True
        else:
            print(f"Incorrect. The correct answer is: {correct_choice_text}\n")
            correct = False
    # append result of the current question to the results variable list
        results.append({
            "question": question["question"],
            "correct": correct
            })
    # retrieve the final score and print to console as well as write to txt file
    final_score = score
    print(f"You're final score is : {final_score}! Your results have been saved on the final_score text file!)")
    with open("C:\\Users\\naomi\\PycharmProjects\\CFG-Assignments\\AssignmentTwo\\final_score.txt", "w") as file:
        file.write(f"You're final score is: {final_score}\n")
        for i, result in enumerate(results):
            file.write(html.unescape(f"Question{i + 1}: {result["question"][:50]}...\n"))
            file.write(html.unescape(f"You're answer was: {result["correct"]}\n"))
    return score

#call the function
play_game()

