import random
import string

def generate_password(length=12, include_lowercase=True, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = ''

    if include_lowercase:
        characters += string.ascii_lowercase

    if include_uppercase:
        characters += string.ascii_uppercase

    if include_digits:
        characters += string.digits

    if include_special_chars:
        characters += string.punctuation

    if length < 1:
        print("Password length should be at least 1.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Example usage:
    password_length = int(input("Enter the desired password length: "))
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    generated_password = generate_password(
        length=password_length,
        include_lowercase=include_lowercase,
        include_uppercase=include_uppercase,
        include_digits=include_digits,
        include_special_chars=include_special_chars
    )

    if generated_password:
        print("Generated Password:", generated_password)
    else:
        print("Password generation failed.")
