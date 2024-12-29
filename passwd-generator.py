import random
import string

def generate_password(length, use_upper, use_lower, use_numbers, use_symbols, name=None):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character types selected. Please try again."
    
    if name:
        
        name_part = ''.join(random.choice(name) for _ in range(min(len(name), length // 2)))
        random_part = ''.join(random.choice(characters) for _ in range(length - len(name_part)))
        return name_part + random_part

  
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include special characters? (y/n): ").lower() == 'y'
        use_name = input("Do you want to base the password on your name? (y/n): ").lower() == 'y'
        
        name = None
        if use_name:
            name = input("Enter your name: ")

        print("\nGenerating 50 passwords...\n")
        for i in range(1, 51):
            password = generate_password(length, use_upper, use_lower, use_numbers, use_symbols, name)
            print(f"Password {i}: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
