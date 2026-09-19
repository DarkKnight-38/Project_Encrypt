from Functions.Action_Hist import push_hist
from Functions.PW_Generator import password_generator
import pickle
import os
import pwinput

VAULT_DIR = os.path.join('Data', 'PWManagerData')

def _ensure_vault_dir():
    os.makedirs(VAULT_DIR, exist_ok=True)

def _get_vault_file(UID):
    _ensure_vault_dir()
    return os.path.join(VAULT_DIR, f'password_vault_{UID}.dat')

def _load_vault(UID):
    file_name = _get_vault_file(UID)
    data = []
    if not os.path.exists(file_name):
        return data

    try:
        with open(file_name, 'rb') as f:
            while True:
                try:
                    entry = pickle.load(f)
                    if isinstance(entry, dict) and 'Website' in entry:
                        data.append(entry)
                except EOFError:
                    break
    except (pickle.UnpicklingError, OSError, IOError) as e:
        print(f"[!] Warning: Error reading vault file ({e}).")
    return data

def _save_vault(UID, data):
    file_name = _get_vault_file(UID)
    try:
        with open(file_name, 'wb') as f:
            for entry in data:
                pickle.dump(entry, f)
        return True
    except (OSError, IOError) as e:
        print(f"[!] Error saving vault file: {e}")
        return False

def add(UID):
    push_hist('[*] Password manager add() was called.')
    data = _load_vault(UID)

    try:
        website = input("Enter the website: ").strip()
        if not website:
            print("[!] Website cannot be empty. Entry not added.")
            return

        for entry in data:
            if entry.get('Website', '').lower() == website.lower():
                print("[!] ERROR: This website already exists in the vault.")
                return

        username = input("Enter the username: ").strip()
        if not username:
            print("[!] Username cannot be empty. Entry not added.")
            return

        password = input("Enter the password (Press Enter to generate a random password): ").strip()
        if not password:
            password = password_generator()
            if not password:
                print("[!] No password generated. Entry aborted.")
                return

        notes = input("Enter any notes (optional): ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Add entry cancelled.")
        return

    details = {
        'Website': website,
        'Username': username,
        'Password': password,
        'Notes': notes,
        'UID': UID
    }
    data.append(details)
    if _save_vault(UID, data):
        print(f"[*] Successfully added entry for '{website}' to the vault.")
        push_hist(f"[*] Added new entry for website: {website} to the password vault.")

def remove(UID, password):
    push_hist('[*] Password manager remove() was called.')
    data = _load_vault(UID)

    if not data:
        print("[i] Password vault is empty.")
        return

    try:
        password_input = pwinput.pwinput(prompt="Enter your account password to remove an entry: ", mask='*').strip()
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Operation cancelled.")
        return

    if password_input != password:
        print("[!] ERROR: Incorrect password. Access denied.")
        push_hist('[!] ERROR: Incorrect password entered for removing an entry from the vault.')
        return

    print("[*] Access granted. You can now remove an entry from the password vault.")
    try:
        website = input("Enter the website to remove: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Operation cancelled.")
        return

    entry_to_remove = None
    for entry in data:
        if entry.get('Website', '').lower() == website.lower():
            entry_to_remove = entry
            break

    if entry_to_remove:
        data.remove(entry_to_remove)
        if _save_vault(UID, data):
            print(f"[*] Removed entry for website: {website} from the password vault.")
            push_hist(f"[*] Removed entry for website: {website} from the password vault.")
    else:
        print(f"[!] ERROR: No entry found for website: {website}.")
        push_hist(f"[!] ERROR: No entry found for website: {website} to remove from the vault.")

def edit(UID, password):
    push_hist('[*] Password manager edit() was called.')
    data = _load_vault(UID)

    if not data:
        print("[i] Password vault is empty.")
        return

    try:
        password_input = pwinput.pwinput(prompt="Enter your account password to edit an entry: ", mask='*').strip()
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Operation cancelled.")
        return

    if password_input != password:
        print("[!] ERROR: Incorrect password. Access denied.")
        push_hist('[!] ERROR: Incorrect password entered for editing an entry.')
        return

    try:
        website = input("Enter the website of the entry to edit: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Operation cancelled.")
        return

    target = None
    for entry in data:
        if entry.get('Website', '').lower() == website.lower():
            target = entry
            break

    if not target:
        print(f"[!] ERROR: No entry found for website: {website}.")
        return

    try:
        new_user = input(f"Enter new username (current: {target['Username']}, leave blank to keep): ").strip()
        if new_user:
            target['Username'] = new_user

        change_pw = input("Do you want to change the password? (y/n): ").strip().lower()
        if change_pw == 'y':
            new_pw = input("Enter new password (Press Enter to generate a random password): ").strip()
            if not new_pw:
                new_pw = password_generator()
            if new_pw:
                target['Password'] = new_pw

        new_notes = input(f"Enter new notes (leave blank to keep current): ").strip()
        if new_notes:
            target['Notes'] = new_notes
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Edit cancelled.")
        return

    if _save_vault(UID, data):
        print(f"[*] Successfully updated entry for '{website}'.")
        push_hist(f"[*] Edited entry for website: {website}.")

def view(UID, password):
    push_hist('[*] Password manager view() was called.')
    data = _load_vault(UID)

    if not data:
        print("[i] Password vault is empty.")
        return

    try:
        password_input = pwinput.pwinput(prompt="Enter your account password to view the vault: ", mask='*').strip()
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Operation cancelled.")
        return

    if password_input != password:
        print("[!] ERROR: Incorrect password. Access denied.")
        push_hist('[!] ERROR: Incorrect password entered for viewing the vault.')
        return

    print(f"\n[*] Access granted. Displaying password vault entries ({len(data)} total):")
    print("-" * 35)
    for entry in data:
        print(f"Website : {entry.get('Website', 'N/A')}")
        print(f"Username: {entry.get('Username', 'N/A')}")
        print(f"Password: {entry.get('Password', 'N/A')}")
        print(f"Notes   : {entry.get('Notes', '')}")
        print("-" * 35)
    print()