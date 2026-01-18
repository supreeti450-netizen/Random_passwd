"""
Project Title: Random Password Generator and Validator using Python

Description:
This project allows users to either generate a random secure password
or enter their own password and check its strength based on security rules.
"""

import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return "Error: No character set selected!"

    return "".join(random.choice(characters) for _ in range(length))


def check_strength(password):
    length = len(password)
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_letter, has_digit, has_symbol])

    if length >= 12 and score == 3:
        return "Strong"
    elif length >= 8 and score >= 2:
        return "Medium"
    else:
        return "Weak"


print("🔐 PASSWORD MANAGER 🔐")
print("1. Generate Random Password")
print("2. Use My Own Password")

choice = input("Choose an option (1/2): ")

if choice == "1":
    try:
        length = int(input("Enter password length: "))
        letters = input("Include letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, letters, numbers, symbols)
        print("\nGenerated Password:", password)
        print("Password Strength:", check_strength(password))

    except ValueError:
        print("Invalid input. Please enter numbers only.")

elif choice == "2":
    user_password = input("Enter your password: ")
    strength = check_strength(user_password)
    print("Password Strength:", strength)

else:
    print("Invalid choice.")
