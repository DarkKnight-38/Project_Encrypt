import csv
import os
import random
import pwinput

USER_DATA_DIR = os.path.join('Data', 'UserData')
USER_DATA_FILE = os.path.join(USER_DATA_DIR, 'user_data.csv')

def _ensure_user_file():
    os.makedirs(USER_DATA_DIR, exist_ok=True)
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Username', 'Password', 'UniqueID'])

def login():
    try:
        print("\n--- USER LOGIN ---")
        username = input('Enter your username: ').strip()
        password = pwinput.pwinput(prompt='Enter your password: ', mask='*').strip()
    except (KeyboardInterrupt, EOFError):
        print('\n[!] Login cancelled.')
        return None, None

    if username == '' or password == '':
        print('[!] Username and password cannot be empty. Login aborted.')
        return None, None

    _ensure_user_file()
    try:
        with open(USER_DATA_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row and len(row) >= 3 and row[0].lower() != 'username':
                    if row[0] == username and row[1] == password:
                        print(f"Logging in as {username}...")
                        print('[*] Login successful!')
                        return row[2], row[1]
    except (OSError, IOError) as e:
        print(f"[!] Error reading user data file: {e}")
        return None, None

    print('[!] Invalid username or password. Login failed.')
    return None, None

def register():
    try:
        print("\n--- USER REGISTRATION ---")
        username = input('Enter a username: ').strip()
    except (KeyboardInterrupt, EOFError):
        print('\n[!] Registration cancelled.')
        return False

    if username == '':
        print('[!] Username cannot be empty. Registration aborted.')
        return False
    elif username.lower() == 'username':
        print('[!] "username" is not allowed as a username. Registration aborted.')
        return False

    _ensure_user_file()
    existing_users = []
    existing_ids = []

    try:
        with open(USER_DATA_FILE, 'r', newline='', encoding='utf-8') as g:
            data = csv.reader(g)
            for row in data:
                if row and len(row) >= 3 and row[0].lower() != 'username':
                    existing_users.append(row[0])
                    existing_ids.append(str(row[2]))
    except (OSError, IOError) as e:
        print(f"[!] Error accessing user data file: {e}")
        return False

    if username in existing_users:
        print('[!] User already exists! Returning to menu...')
        return False

    try:
        password = pwinput.pwinput(prompt='Enter a password: ', mask='*').strip()
        if password == '':
            print('[!] Password cannot be empty. Registration aborted.')
            return False

        re_password = pwinput.pwinput(prompt='Enter the password again: ', mask='*').strip()
    except (KeyboardInterrupt, EOFError):
        print('\n[!] Registration cancelled.')
        return False

    if password != re_password:
        print('[!] Re-entered password does not match. Registration failed.')
        return False

    while True:
        unique_id = str(random.randint(10000000, 99999999))
        if unique_id not in existing_ids:
            break

    try:
        with open(USER_DATA_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([username, password, unique_id])
        print('[*] User registered successfully!')
        return True
    except (OSError, IOError) as e:
        print(f"[!] Error saving user data: {e}")
        return False