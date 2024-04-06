def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return False
    
    # Uppercase and lowercase letters check
    has_uppercase = False
    has_lowercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
    if not has_uppercase or not has_lowercase:
        return False
    
    # Digit check
    has_digit = False
    for integer in password:
        if integer.isdigit():
            has_digit =True
    if not has_digit:
        return False
    
    # Special character check
    has_special_char = False
    special_characters = "!@#$%^&*()-_=+"
    for symbol in password:
        for char in special_characters:
            if symbol == char:
                has_special_char = True
    if not has_special_char:
        return False
    
    return True

def main():
    password = input("Enter your password: ")
    if check_password_strength(password):
        print("Password is strong!")
    else:
        print("Password is weak. Please ensure it meets the criteria.")

if __name__ == "__main__":
    main()
