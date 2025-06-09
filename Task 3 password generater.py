import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Welcome to the Advanced Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return
        
        print("\nChoose password complexity options:")
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        if "Error" in password:
            print(password)
            return

        print(f"\nGenerated Password: {password}")

        save_option = input("\nDo you want to save this password to a file? (y/n): ").lower()
        if save_option == 'y':
            with open("saved_password.txt", "a") as file:
                file.write(password + "\n")
            print("Password saved to 'saved_password.txt'.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
