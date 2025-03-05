#Write a python function that takes input of characters separated by commas and then sort them alphabetically.

def sort_characters(input_str):
    chars = input_str.split(",")
    sort_chars = sorted([char.strip() for char in chars])
    
    return ",".join(sort_chars)

input_str = "d,y,b,r"
print(sort_characters(input_str))