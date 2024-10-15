import requests
import pprint

def get_all_recipes_front_end():
    try:
        endpoint = "http://127.0.0.1:5000/recipes"
        data = requests.get(endpoint).json()
        return data
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON")

def get_all_recipes_with_id():
    try:
        endpoint = "http://127.0.0.1:5000/recipes/id"
        data = requests.get(endpoint).json()
        return data
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON")

def get_breakfast_recipes_front_end():
    endpoint = "http://127.0.0.1:5000/recipes/breakfast"
    data = requests.get(endpoint).json()
    return data

def get_lunch_recipes_front_end():
    endpoint = "http://127.0.0.1:5000/recipes/lunch"
    data = requests.get(endpoint).json()
    return data

def get_dinner_recipes_front_end():
    endpoint = "http://127.0.0.1:5000/recipes/dinner"
    data = requests.get(endpoint).json()
    return data

def delete_recipe_by_id_front_end(id):
    endpoint = f"http://127.0.0.1:5000/recipes/remove/{id}"
    result = requests.delete(endpoint).json()
    return result

def run():
    print('Hello, and welcome to your nutrition database')
    print('You can use this database to get recipe ideas for your day, you can also delete any you dont like.')
    answer = input('Would you like to view all recipes or by meal type? Choose A for All or B for by meal type? ').strip().upper()

    if answer == 'A':
        pprint.pp(get_all_recipes_front_end())

    elif answer == 'B':
        print('Ok, lets take a look')
        user_answer = input('What would you like to browse? Breakfast, lunch or dinner? ').lower()
        if user_answer == 'breakfast':
            pprint.pp(get_breakfast_recipes_front_end())
        elif user_answer == 'lunch':
            pprint.pp(get_lunch_recipes_front_end())
        elif user_answer == 'dinner':
            pprint.pp(get_dinner_recipes_front_end())
        else:
            print('Invalid option. Please select either breakfast, lunch, or dinner.')

    else:
        print('Please choose a valid option: either A or B!')

    print('If there is a recipe you dont like you can delete it!')
    user_delete = input('If you would like to delete a recipe press Y, if not click N ').strip().upper()

    if user_delete == 'Y':
        pprint.pp(get_all_recipes_with_id())
        user_choice = input('Please enter the id of the recipe you would like to delete! ')
        pprint.pp(delete_recipe_by_id_front_end(user_choice))

    elif user_delete == 'N':
        print('Ok, have a nice day!')

    else:
        print('Please choose a valid option, either Y or N ')


if __name__ == "__main__":
    run()