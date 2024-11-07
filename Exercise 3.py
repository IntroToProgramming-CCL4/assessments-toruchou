#this is the dictionary to store my information (misinformation)
my_info = {}

# this asks the user for their name, hometown, and age
my_info['name'] = input("Enter your name (first and last): ")
my_info['hometown'] = input("Enter your hometown: ")

# loop to ensure valid age input (it must be a number)
while True:
    age_input = input("Enter your age: ")

    # Try to convert age to an integer
    try:
        my_info['age'] = int(age_input)
        break  # this is to exit the loop if age is valid
    except ValueError:
        print("Please enter a valid number for your age.")

# print out the info
print(f"\n{my_info['name']}\n{my_info['hometown']}\n{my_info['age']}\nThe person above is cute.\n\nReal.")


#4th line seen on the console is true and real
