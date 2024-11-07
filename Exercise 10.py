import time
import sys

# function to check if the number is even or odd
def even_odd_checker(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# main function
def main():
    while True: # loops main until input is valid
        try:
            user_input = int(input("Enter a number: "))
            
            # unnecessary loading :3
            for i in range(4):
                dots = "." * i
                sys.stdout.write(f"\rloading{dots}")
                sys.stdout.flush()
                time.sleep(0.6)
            print()

            # passes the number to the even_odd_checker function and prints the result
            print(even_odd_checker(user_input))
            break
        except ValueError: # makes sure that the user enters an integer
            print("That's not a valid number!")

# call the main function (yes, I also use a main guard on my scripts if necessary hehe)
if __name__ == "__main__":
    main()
