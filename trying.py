import random
import string
import sys

def generate_infinite_list(filename="wordlist.txt"):
    prefix = "CLB"
    generated_count = 0
    
    print(f"Generating strings into {filename}...")
    print("Press Ctrl+C to stop at any time.")
    
    try:
        # 'a' opens the file for appending; 'w' would overwrite it
        with open(filename, "a") as f:
            while True:
                # 1. Define pools
                digits_pool = list(string.digits)
                letters_pool = [c for c in string.ascii_uppercase if c not in prefix]
                
                # 2. Pick unique characters (4 digits, 3 letters)
                random_digits = random.sample(digits_pool, 4)
                random_letters = random.sample(letters_pool, 3)
                
                # 3. Mix and combine
                suffix = random_digits + random_letters
                random.shuffle(suffix)
                
                # 4. Write to file immediately
                final_string = prefix + "".join(suffix)
                f.write(final_string + "\n")
                
                generated_count += 1
                
                # Visual feedback every 1000 strings
                if generated_count % 1000 == 0:
                    print(f"Total generated: {generated_count}", end="\r")
                    
    except KeyboardInterrupt:
        print(f"\nStopped by user. Total strings added to {filename}: {generated_count}")
        sys.exit()

if __name__ == "__main__":
    generate_infinite_list()
    
    
