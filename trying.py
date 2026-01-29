import itertools
import string

# Fixed prefix
prefix = "CLB"

# Allowed characters: CAPITAL letters + digits
chars = string.ascii_uppercase + string.digits

remaining_length = 7
output_file = "CLB_2LETTER_REPEAT_ALLOWED.txt"

def valid_word(word):
    for i in range(len(word) - 2):
        # If three consecutive letters are same → invalid
        if word[i].isalpha() and word[i+1].isalpha() and word[i+2].isalpha():
            if word[i] == word[i+1] == word[i+2]:
                return False
    return True

with open(output_file, "w") as f:
    for combo in itertools.product(chars, repeat=remaining_length):
        full_word = prefix + "".join(combo)
        if valid_word(full_word):
            f.write(full_word + "\n")

print("Wordlist generated successfully!")
print("Saved as:", output_file)
