import random
import string

def generate_and_save():
    # 1. Fixed Prefix
    prefix = "CLB"
    
    # 2. Define character pools
    # We exclude C, L, and B from the letter pool to ensure total uniqueness
    digits_pool = list(string.digits)
    letters_pool = [c for c in string.ascii_uppercase if c not in prefix]
    
    # 3. Pick 4 unique digits and 3 unique letters
    random_digits = random.sample(digits_pool, 4)
    random_letters = random.sample(letters_pool, 3)
    
    # 4. Combine and shuffle the last 7 characters
    suffix_chars = random_digits + random_letters
    random.shuffle(suffix_chars)
    
    # 5. Create the final 10-character string
    final_string = prefix + "".join(suffix_chars)
    
    # 6. Save to a .txt file
    try:
        with open("output.txt", "w") as file:
            file.write(final_string)
        print(f"Success! String '{final_string}' saved to output.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_and_save()
    
