def strength_test():
    print("\n--- PASSWORD STRENGTH TEST ---")

    try:
        password = input("Enter your password to begin the evaluation: ")
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Password evaluation cancelled.")
        return

    if not password:
        print("[!] Password cannot be empty.")
        return

    score = 0
    feedback = []

    password_length = len(password)
    if password_length >= 8:
        score += 1
    else:
        feedback.append('[!] Try increasing the length of your password to at least 8 characters.')

    has_upper = any(char.isupper() for char in password)
    if has_upper:
        score += 1
    else:
        feedback.append('[!] Try adding uppercase letters to your password.')

    has_lower = any(char.islower() for char in password)
    if has_lower:
        score += 1
    else:
        feedback.append('[!] Try adding lowercase letters to your password.')

    has_digit = any(char.isdigit() for char in password)
    if has_digit:
        score += 1
    else:
        feedback.append('[!] Try adding digits to your password.')

    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    has_special = any(char in special_characters for char in password)
    if has_special:
        score += 1
    else:
        feedback.append('[!] Try adding special characters to your password.')

    print("\n--- RESULTS ---")
    print(f"Final Score: {score} out of 5")

    if score == 5:
        print("Password strength: Very Strong")
        print("[*] No changes needed, your password is very strong!")
    elif score in (3, 4):
        print("Password strength: Strong")
    elif score == 2:
        print("Password strength: Weak")
    else:
        print("Password strength: Very Weak")

    if feedback:
        print("\n--- SUGGESTIONS FOR IMPROVEMENT ---")
        for tip in feedback:
            print(tip)
    else:
        print("\nGreat job creating a secure password!")