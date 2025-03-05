def print_numbers_skip_7():
    for num in range(1, 51):
        if num % 7 == 0:
            continue
        print(num)

print_numbers_skip_7()
