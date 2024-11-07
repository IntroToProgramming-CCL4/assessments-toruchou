import time
import random

# these are random responses when the user gets the wrong aswer
responses = [
    "Nice try, but nope.",
    "Oof, that's not it.",
    "oh come on, you can do better.",
    "Bruh, really?"
]

# this prints the question, but with a dramatic pause xd
print("Thinking...")
time.sleep(2)
answer = input("What is the capital of Japan? ").strip().lower()

# checks if the answer is correct or nah and gives a response
if answer == "tokyo":
    time.sleep(1)
    print("Niceu, you're correct! Tokyo is the capital of Japan.")
else:
    # this picks a random response in the dictionary
    print(random.choice(responses))
    time.sleep(1)
    print("The correct answer is Tokyo!")