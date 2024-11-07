import time
import random

# Tis is the list of east asian countries and their capitals
countries_and_capitals = {
    "china": "beijing",
    "japan": "tokyo",
    "south korea": "seoul",
    "north korea": "pyongyang",
    "taiwan": "taipei",
    "mongolia": "ulaanbaatar",
}

# random responses when the user gets the wrong answer
responses = [
    "Nice try, but nope.",
    "Oof, that's not it.",
    "Oh come on, you can do better.",
    "Bruh, really?"
]

score = 0

# function to ask the user the capital of a country
def ask_question(country, capital):
    global score
    print(f"\nWhat is the capital of {country.title()}?")
    time.sleep(2)
    answer = input().strip().lower()

    if answer == capital:
        time.sleep(1)
        print(f"Niceu, you're correct! {capital.title()} is the capital of {country.title()}.")
        score += 1 # adds 1 score since correct
    else:
        print(random.choice(responses))
        time.sleep(1)
        print(f"The correct answer is {capital.title()}!")

# starting msg
print("This is the East Asian Capitals Quiz!")
time.sleep(1)

# loop through each country in the dictionary and ask the user
for country, capital in countries_and_capitals.items():
    ask_question(country, capital)

# prints the final message and the user's score
print(f"\nQuiz complete! You answered all the questions.\nYour final score is {score}/6!")
