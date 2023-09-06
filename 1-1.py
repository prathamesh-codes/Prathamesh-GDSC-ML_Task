import random
import string

def generate_password(length=12, upper=True, lower=True, digits=True, special=True):
    uppercase_chars = string.ascii_uppercase if upper else ""
    lowercase_chars = string.ascii_lowercase if lower else ""
    digits = string.digits if digits else ""
    special_chars = string.punctuation if special else ""

    characters = uppercase_chars + lowercase_chars + digits + special_chars

    if not characters:
        print("Please select at least one character type.")
        return

    length = max(length, 4)

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

pass_length = int(input("Enter the length of the password: "))
uppercase = input("Include uppercase characters? (y for yes/n for no): ").lower() == 'y'
lowercase = input("Include lowercase characters? (y for yes/n for no): ").lower() == 'y'
digits = input("Include digits? (y for yes/n for no): ").lower() == 'y'
special_chars = input("Include special characters? (y for yes/n for no): ").lower() == 'y'

password = generate_password(length=pass_length,upper=uppercase,lower=lowercase,digits=digits,special=special_chars)

if password:
    print("Generated Password:", password)

