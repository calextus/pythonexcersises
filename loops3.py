#3. Declare a list in python and then write a program which finds the largest number in that list using a loop.
numbers = [12, 45, 78, 23, 56, 89, 34, 99, 67, 88]
largest = numbers[0]  # Assume the first number is the largest

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)
