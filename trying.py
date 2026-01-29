import random
import string
import sys

def generate_strict_wordlist(filename="wordlist.txt"):
    prefix = "CLB"
    generated_count = 0
    
    print(f"Generating strings into {filename}...")
    print("Press Ctrl+C to stop.")
    
    try:
        with open(filename, "a") as f:
            while True:
                # 1. Prepare pools (excluding C, L, B for safety)
                digits_pool = list(string.digits)
                letters_pool = [c for c in string.ascii_uppercase if c not in prefix]
                
                # 2. Pick the mandatory 4 digits and 3 letters first to ensure uniqueness
                chosen_digits = random.sample(digits_pool, 4)
                chosen_letters = random.sample(letters_pool, 3)
                
                # 3. Assign the fixed positions
                # 4th char (index 3) must be a digit
                fourth_char = chosen_digits.pop() 
                # Last char (index 9) must be a letter
                last_char = chosen_letters.pop()
                
                # 4. Mix the remaining 5 characters (3 digits, 2 letters) for the middle
                middle_pool = chosen_digits + chosen_letters
                random.shuffle(middle_pool)
                middle_section = "".join(middle_pool)
                
                # 5. Assemble: CLB + Digit + 5 Mixed + Letter
                final_string = f"{prefix}{fourth_char}{middle_section}{last_char}"
                
                f.write(final_string + "\n")
                generated_count += 1
                
                if generated_count % 1000 == 0:
                    print(f"Total generated: {generated_count}", end="\r")
                    
    except KeyboardInterrupt:
        print(f"\nStopped. Total added: {generated_count}")

if __name__ == "__main__":
    generate_strict_wordlist()
                
