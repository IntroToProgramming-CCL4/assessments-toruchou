# dictionary for the days in months
month_days = {
    1: 31,
    2: 28,  # Will be adjusted if it's leap year
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

# input for year
year = int(input("Enter the year: "))

# checks if year input equals to a leap year, if so, change days of Feb to 29
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    month_days[2] = 29

# checks if the month number is valid
while True:
    month_num = int(input("Enter the month number (1-12): "))
    if 1 <= month_num <= 12:
        print(f"The number of days in {month_name[month_num]} {year} is {month_days[month_num]}")
        break
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")

# leap years don't exist (controversial opinion) jk
