import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special_chars else ""

    
    all_characters = lowercase + uppercase + numbers + special_chars

    
    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    
    try:
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
