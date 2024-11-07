# dictionary for the days in months (exculding leap years... for now)
month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# dictionary to distinguish the month from the number
month_name = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

month_num = int(input("Enter the month number (1-12): "))

# checks if the input is valid and print the number of days in that month
if 1 <= month_num <= 12:
    print(f"The number of days in {month_name[month_num]} is {month_days[month_num]}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
