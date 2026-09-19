import secrets
import os
import hashlib
import pickle
import random

def _prepare_filepath(filename, default_ext):
    filename = str(filename).strip()
    if not filename:
        return ""
    if not filename.lower().endswith(default_ext.lower()):
        filename += default_ext
    directory = os.path.dirname(filename)
    if directory:
        os.makedirs(directory, exist_ok=True)
    return filename

def min_encrypt(encrypted_file, encryption_key_file, text, uid):
    if not text:
        print("[!] ERROR: Text to encrypt cannot be empty.")
        return False

    encrypted_file = _prepare_filepath(encrypted_file, '.txt')
    encryption_key_file = _prepare_filepath(encryption_key_file, '.dat')

    if not encrypted_file or not encryption_key_file:
        print("[!] ERROR: Filenames cannot be empty.")
        return False

    if os.path.exists(encrypted_file):
        print(f"[!] WARNING: The file '{encrypted_file}' already exists and will be overwritten.")
    if os.path.exists(encryption_key_file):
        print(f"[!] WARNING: The file '{encryption_key_file}' already exists and will be overwritten.")

    keys = []
    encrypted_chars = []
    for char in text:
        random_shift = random.randint(-20, 20)
        keys.append(random_shift)
        encrypted_chars.append(chr(ord(char) + random_shift))

    encrypted_text = "".join(encrypted_chars)

    try:
        with open(encrypted_file, 'w', encoding='utf-8') as f_txt:
            f_txt.write(encrypted_text)

        with open(encryption_key_file, 'wb') as f_bin:
            payload = {'keys': keys, 'uniqueid': uid}
            pickle.dump(payload, f_bin)
    except (OSError, IOError, PermissionError) as e:
        print(f"[!] ERROR: Failed to write encrypted files: {e}")
        return False

    print("\n[*] SUCCESS: Data Encrypted.")
    print(f" > Ciphertext written to : {encrypted_file}")
    print(f" > Keys & UID written to : {encryption_key_file}\n")
    return True

def inter_encrypt():
    print("[i] Intermediate encryption is not yet implemented.")

def max_encrypt(text, encrypted_file, encryption_key_file, UID):
    if not text:
        print("[!] ERROR: Text to encrypt cannot be empty.")
        return False

    encrypted_file = _prepare_filepath(encrypted_file, '.txt')
    encryption_key_file = _prepare_filepath(encryption_key_file, '.dat')

    if not encrypted_file or not encryption_key_file:
        print("[!] ERROR: Filenames cannot be empty.")
        return False

    if os.path.exists(encrypted_file):
        print(f"[!] WARNING: The file '{encrypted_file}' already exists and will be overwritten.")
    if os.path.exists(encryption_key_file):
        print(f"[!] WARNING: The file '{encryption_key_file}' already exists and will be overwritten.")

    text_bytes = text.encode('utf-8')
    og_hash = hashlib.sha256(text_bytes).hexdigest()

    keys = [secrets.randbelow(256) for _ in text]
    encrypted_integers = [ord(char) ^ key for char, key in zip(text, keys)]
    hex_formatted_ciphertext = bytearray(encrypted_integers).hex()

    security_payload = {
        'keys': keys,
        'signature': og_hash,
        'uniqueid': UID
    }

    try:
        with open(encrypted_file, 'w', encoding='utf-8') as f_txt:
            f_txt.write(hex_formatted_ciphertext)

        with open(encryption_key_file, 'wb') as f_bin:
            pickle.dump(security_payload, f_bin)
    except (OSError, IOError, PermissionError) as e:
        print(f"[!] ERROR: Failed to write encrypted files: {e}")
        return False

    print("\n[*] SUCCESS: Data Encrypted.")
    print(f" > Ciphertext written to : {encrypted_file}")
    print(f" > Keys & Hash written to: {encryption_key_file}\n")
    return True