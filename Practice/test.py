# country_capitals = {
#   "Germany": "Berlin",
#   "Canada": "Ottawa",
#   "England": "London"
# }
#
# print(country_capitals.keys())
# print(country_capitals.values())

# __ Time Left to Live __
#
# Take a users input, in date format, of their date of birth (DDMMYYYY).
# Then take that users life expectancy.
#
# Provide them with the dire news of how long they have left to live.
#
# Provide the news in the format of;
# - First: Years left to live
# - Second: Minutes left to live
# - Third: Seconds left to live
#
# ### OPTIONAL ###
# Write the life expectancy report to a text file.

# import datetime
# CurrentDate=datetime.date.today()
# print(CurrentDate.strftime("%d/%b/%Y"))

# birthday = input("What is your birthday? (DD/MM/YYYY)")
# birthdate=datetime.datetime.strptime(birthday,"%d/%m/%Y").date()
# print("Your birthday is : "+birthdate.strftime('%d/%B/%Y'))
#
# death = input("When do you expect to die? (DD/MM/YYYY)")
# death_date = datetime.datetime.strptime(death, "%d/%m/%Y").date()
# print("You are expecting to die: "+death_date.strftime('%d/%m/%Y'))
#
# def time_left_to_live():
#   days_left = death_date - CurrentDate
#   years_left = days_left/365
#   print(f"You have: {years_left} time left to live.")
#
# time_left_to_live()

user_step = 1

steps = [{
    "id": 0,
    "text": "you are at a location",
    "option_one": {
        "text": "Your option here",
        "outcome": 2
    },
    "option_two": {
        "text": "Your second option here",
        "outcome": 3
    }
}]

while user_step > 0:
    # build program here
it_begins = input("You are going for a walk but it looks like it might rain. Do you want to take an umbrella?")

    # set step to 0 at the end to exit