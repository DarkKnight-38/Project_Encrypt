def strength_test():#Raphael #Complete
    print("\n--- PASSWORD STRENGTH TEST ---")
    score = 0
    password = input("Enter your password: ")
    e=''
    # Check for length
    if len(password) >= 8:
        score += 1
    else:
        e+='[!] Try increasing the length of your password to at least 8 characters.\n'

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        e+='[!]Try adding uppercase letters to your password.\n'

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        e+='[!] Try adding lowercase letters to your password.\n'

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1 
    else:
        e+='[!] Try adding digits to your password.\n'

    # Check for special characters
    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    if any(char in special_characters for char in password):
        score += 1
    else:
        e+='[!] Try adding special characters to your password.\n'

    # Determine strength level
    if score == 5:
        print("Password strength: Very Strong")
        print("[*] No changes needed, your password is very strong!")
    elif score == 4 or score == 3:
        print("Password strength: Strong")
    elif score == 2:
        print("Password strength: Weak")
    else:
        print("Password strength: Very Weak")

    print(e)
