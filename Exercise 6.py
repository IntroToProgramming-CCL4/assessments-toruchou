import time

# This is case sensitive
correct_password = "GothMommy"

# maximum number of attempts
max_attempts = 3
attempts = 0

# this is a loop to repeatedly ask the user to enter the password
while True:
    input_password = str(input("Password: "))

    # this checks if the entered password is correct
    if input_password == correct_password:
        print("Access granted.")
        break  # exits the loop once the correct password is entered
    else:
        attempts += 1
        print("Incorrect password. Try again.")
        
        # reports to the authorities if total attempts have reached 9
        if attempts >= 9:
            print("You have reached the maximum amount of attempts, we will now report this to the authorities.")
            break
        
        # this is a lock feature to prevent the user to spam password attempts
        if attempts >= max_attempts:
            print("You have entered the wrong password too many times. Please wait 30 seconds.")
            time.sleep(30)
            max_attempts += 3  # this gives the user more attempts after the cooldown is finished