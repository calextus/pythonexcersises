def print_day_of_week(day):
    match day:
        case 1:
            print("The day is Monday")
        case 2:
            print("The day is Tuesday")
        case 3:
            print("The day is Wednesday")
        case 4:
            print("The day is Thursday")
        case 5:
            print("The day is Friday")
        case 6:
            print("The day is Saturday")
        case 7:
            print("The day is Sunday")
        case _:
            print("Invalid input! Please enter a number between 1 and 7.")

# Example usage
user_input = int(input("Enter a number (1-7) to get the day of the week: "))
print_day_of_week(user_input)
