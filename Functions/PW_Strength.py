def strength_test():
    
    print("--- PASSWORD STRENGTH TEST ---")

    score = 0
    password = input("Enter your password to begin the evaluation: ")
    e = ''

    password_length = len(password)
    
    if password_length >= 8:
        score += 1
    else:
        e += '[!] Try increasing the length of your password to at least 8 characters.\n'

    has_upper = False
    
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if has_upper == True:
        score += 1
    else:
        e += '[!] Try adding uppercase letters to your password.\n'

    has_lower = False
    
    for char in password:
        if char.islower():
            has_lower = True
            break

    if has_lower == True:
        score += 1
    else:
        e += '[!] Try adding lowercase letters to your password.\n'

    has_digit = False
    
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if has_digit == True:
        score += 1
    else:
        e += '[!] Try adding digits to your password.\n'

    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    has_special = False
    
    for char in password:
        if char in special_characters:
            has_special = True
            break

    if has_special == True:
        score += 1
    else:
        e += '[!] Try adding special characters to your password.\n'

    print("\n--- RESULTS ---")
    print(f"Final Score: {score} out of 5")

    if score == 5:
        print("Password strength: Very Strong")
        print("[*] No changes needed, your password is very strong!")
    elif score == 4 or score == 3:
        print("Password strength: Strong")
    elif score == 2:
        print("Password strength: Weak")
    else:
        print("Password strength: Very Weak")

    if e != '':
        print("\n--- SUGGESTIONS FOR IMPROVEMENT ---")
        print(e)
    else:
        print("\nGreat job creating a secure password!")