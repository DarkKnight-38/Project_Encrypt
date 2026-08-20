import csv
import os
def login():#Sasank
    pass

def register():  # Raphael
    print('\n--- NEW USER REGISTRATION ---')
    
    # 1. Ask for username and check if it's empty
    username = input('Enter a username: ').strip()
    if username == '':
        print('[!] Username cannot be empty. Registration aborted.')
        return

    # 2. Safely read existing users to prevent duplicates
    existing_users = []
    if os.path.exists('user_data.csv'):
        with open('user_data.csv', 'r', newline='') as g:
            data = csv.reader(g)
            for row in data:
                if row:  # Ensure the row isn't blank
                    existing_users.append(row[0])
                    
    if username in existing_users:
        print('[!] User already exists! Returning to menu...')
        return

    # 3. Ask for password and check if it's empty
    password = input('Enter a password: ').strip()
    if password == '':
        print('[!] Password cannot be empty. Registration aborted.')
        return

    # 4. The 3-Attempt Password Verification Loop
    attempts = 3
    re_password = input('Enter the password again: ').strip()
    
    while password != re_password and attempts > 1:
        attempts -= 1
        print(f'[!] Passwords do not match. You have {attempts} attempts left.')
        re_password = input('Re-enter the password: ').strip()

    # If they run out of attempts, kick them back to the start
    if password != re_password:
        print('[!] Maximum attempts reached. Registration failed. Please start over.')
        return

    # 5. If we reach this line, the password is verified! Add them to the CSV.
    with open('user_data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password])
        
    print('[*] User registered successfully!')

register()