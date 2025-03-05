def arrange_chars(word):
    """Arranges the characters of the word in alphabetical order."""
    return "".join(sorted(word))

def check_length(word):
    """Returns True if the word has more than 5 characters, otherwise False."""
    return len(word) > 5

# Get user input
word = input("Enter a word: ")

# Process the word
sorted_word = arrange_chars(word)
length_check = check_length(word)

# Output results
print(f"Alphabetically arranged: {sorted_word}")
print(f"Has more than 5 characters: {length_check}")
