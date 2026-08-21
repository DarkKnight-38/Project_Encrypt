import csv
import os
import random
import pwinput
def login():#Sasank
   pass

def register():  # Raphael
    print("\n--- USER REGISTRATION ---")
    username = input('Enter a username: ').strip()
    if username == '':
        print('[!] Username cannot be empty. Registration aborted.')
        return
    elif username.lower() == 'username':
        print('[!] "username" is not allowed as a username. Registration aborted.')
        return

 
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

  
    password = pwinput.pwinput(prompt='Enter a password: ', mask='*').strip()
    if password == '':
        print('[!] Password cannot be empty. Registration aborted.')
        return

    attempts = 3
    re_password = pwinput.pwinput(prompt='Enter the password again: ', mask='*').strip()
   
    while password != re_password and attempts > 1:
        attempts -= 1
        print(f'[!] Passwords do not match. You have {attempts} attempts left.')
        re_password = pwinput.pwinput(prompt='Re-enter the password: ', mask='*').strip()

 
    if password != re_password:
        print('[!] Maximum attempts reached. Registration failed. Please start over.')
        return

    existing_ids = []
    while True:
        unique_id = random.randint(10000000, 99999999)
        if unique_id not in existing_ids:
            existing_ids.append(unique_id)
            break
    
  
    with open('user_data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password, unique_id])
       
    print('[*] User registered successfully!')
    


register()

def logout():#Raphael
    pass

def clear_user_data():#Sasank
    pass