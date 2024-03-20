def get_season(month, day):
    seasons = {
        'Spring': (3, 20),
        'Summer': (6, 21),
        'Fall': (9, 22),
        'Winter': (12, 21)
    }

    if (month, day) >= seasons['Winter'] or (month, day) < seasons['Spring']:
        return 'Winter'
    elif (month, day) >= seasons['Spring'] and (month, day) < seasons['Summer']:
        return 'Spring'
    elif (month, day) >= seasons['Summer'] and (month, day) < seasons['Fall']:
        return 'Summer'
    else:
        return 'Fall'
try:
    month = input("Enter the month (e.g., Jan, Feb, Mar, etc.): ")
    day = int(input("Enter the day of the month: "))
    valid_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if month not in valid_months:
        print("Invalid month. Please enter a valid month abbreviation (e.g., Jan, Feb, Mar, etc.).")
    else:
        season = get_season(month, day)
        print(f"The season for {month} {day} is {season}.")
except ValueError:
    print("Invalid input. Please enter a valid day of the month (integer).")
