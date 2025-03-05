#If else statements
#1. The average pass mark for a student is 50%. Write a code for a program that requires the user to enter the student mark.
#If the mark is less than 50%, then output is ''fail'', if mark is 50% - 60% output is ''average pass' and any mark from 61% to 100% output is ''pass''.

mark = int( input("Enter mark : "))

#if statements
if mark < 50 and mark > 0:
    print("Fail")
elif 50 <= mark <= 60:
    print("Average Pass")
elif 61 <= mark <= 100:
    print("Pass")
elif mark < 0:
    print("Invalid mark. Please enter a value between 0 and 100.")
