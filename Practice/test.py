# country_capitals = {
#   "Germany": "Berlin",
#   "Canada": "Ottawa",
#   "England": "London"
# }
#
# print(country_capitals.keys())
# print(country_capitals.values())

import requests
import json
import random


# Get trivia questions from Open Trivia API
def get_trivia_questions(amount=5, difficulty='easy'):
  url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()['results']
  else:
    print("Error fetching trivia questions")
    return []


# Display trivia questions and collect user's answers
def play_trivia(questions):
  score = 0
  for i, question in enumerate(questions):
    print(f"\nQuestion {i + 1}: {question['question']}")
    choices = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(choices)

    for idx, choice in enumerate(choices):
      print(f"{idx + 1}. {choice}")

    user_answer = input("Enter the number of your answer: ")

    if choices[int(user_answer) - 1] == question['correct_answer']:
      print("Correct!")
      score += 1
    else:
      print(f"Wrong! The correct answer was {question['correct_answer']}")

  return score


# Save the final score to a text file
def save_score_to_file(score, total_questions):
  with open("final_score.txt", "w") as file:
    file.write(f"Your final score is: {score} out of {total_questions}\n")
  print("Your score has been saved to 'final_score.txt'.")


# Main function to run the trivia game
def main():
  print("Welcome to the Trivia Game!")
  num_questions = int(input("How many questions would you like to answer? "))
  difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

  questions = get_trivia_questions(amount=num_questions, difficulty=difficulty)
  if not questions:
    print("No questions available.")
    return

  score = play_trivia(questions)
  print(f"\nYour final score is: {score} out of {num_questions}")

  # Save the final score to a file
  save_score_to_file(score, num_questions)


if __name__ == "__main__":
  main()
