import os
import hashlib
import pickle

def _resolve_filepath(filename, default_ext):
    filename = str(filename).strip()
    if not filename:
        return ""
    if not filename.lower().endswith(default_ext.lower()):
        filename += default_ext
    return filename

def min_decrypt(encrypted_file, encryption_key_file, uid):
    encrypted_file = _resolve_filepath(encrypted_file, '.txt')
    encryption_key_file = _resolve_filepath(encryption_key_file, '.dat')

    if not os.path.exists(encrypted_file):
        print(f"[!] ERROR: Encrypted text file not found: {encrypted_file}")
        return False
    if not os.path.exists(encryption_key_file):
        print(f"[!] ERROR: Key file not found: {encryption_key_file}")
        return False

    try:
        with open(encrypted_file, 'r', encoding='utf-8') as f_txt:
            ciphertext_string = f_txt.read()
    except (OSError, IOError) as e:
        print(f"[!] ERROR: Failed to read encrypted text file: {e}")
        return False

    try:
        with open(encryption_key_file, 'rb') as f_bin:
            security_payload = pickle.load(f_bin)
    except (pickle.UnpicklingError, EOFError, OSError, IOError) as e:
        print(f"[!] ERROR: Failed to read or parse key file: {e}")
        return False

    if not isinstance(security_payload, dict) or 'keys' not in security_payload or 'uniqueid' not in security_payload:
        print("[!] ERROR: Key file format is invalid or corrupted.")
        return False

    keys = security_payload['keys']
    saved_uid = security_payload['uniqueid']

    print(f"[*] Verifying file ownership... (Current UID: {uid})")
    if str(uid) != str(saved_uid):
        print("\n[!] ACCESS DENIED: File is watermarked to a different UID.")
        print("[!] You do not have authorization to decrypt this file.")
        print("=" * 50)
        return False

    if len(ciphertext_string) != len(keys):
        print("[!] WARNING: Ciphertext length does not match key length. File may be incomplete or corrupted.")

    try:
        decrypted_chars = [chr(ord(char) - key) for char, key in zip(ciphertext_string, keys)]
        decrypted_text = "".join(decrypted_chars)
    except Exception as e:
        print(f"[!] ERROR during decryption: {e}")
        return False

    print("[*] DECRYPTION COMPLETE. (Min Encryption Mode)")
    print(f"\n--- DECRYPTED PAYLOAD ---\n{decrypted_text}\n-------------------------")
    return True

def inter_decrypt():
    print("[i] Intermediate decryption is not yet implemented.")

def max_decrypt(encrypted_file, encryption_key_file, current_uid):
    encrypted_file = _resolve_filepath(encrypted_file, '.txt')
    encryption_key_file = _resolve_filepath(encryption_key_file, '.dat')

    if not os.path.exists(encrypted_file):
        print(f"[!] ERROR: Encrypted file not found: {encrypted_file}")
        return False
    if not os.path.exists(encryption_key_file):
        print(f"[!] ERROR: Key file not found: {encryption_key_file}")
        return False

    try:
        with open(encrypted_file, 'r', encoding='utf-8') as f_txt:
            hex_ciphertext = f_txt.read().strip()
    except (OSError, IOError) as e:
        print(f"[!] ERROR: Failed to read ciphertext file: {e}")
        return False

    try:
        with open(encryption_key_file, 'rb') as f_bin:
            security_payload = pickle.load(f_bin)
    except (pickle.UnpicklingError, EOFError, OSError, IOError) as e:
        print(f"[!] ERROR: Failed to read or parse key file: {e}")
        return False

    if not isinstance(security_payload, dict):
        print("[!] ERROR: Key file payload is invalid.")
        return False

    for required_field in ('keys', 'signature', 'uniqueid'):
        if required_field not in security_payload:
            print(f"[!] ERROR: Key file is corrupted (missing '{required_field}').")
            return False

    keys = security_payload['keys']
    saved_signature = security_payload['signature']
    saved_uid = security_payload['uniqueid']

    print(f"[*] Verifying file ownership... (Current UID: {current_uid})")
    if str(current_uid) != str(saved_uid):
        print("\n[!] ACCESS DENIED: File is watermarked to a different UID.")
        print("[!] You do not have authorization to decrypt this file.")
        print("=" * 50)
        return False

    try:
        encrypted_bytes = bytearray.fromhex(hex_ciphertext)
    except ValueError:
        print("[!] ERROR: Ciphertext file does not contain valid hexadecimal data.")
        return False

    if len(encrypted_bytes) != len(keys):
        print("[!] WARNING: Ciphertext byte count does not match key count. Data may be corrupted.")

    try:
        decrypted_chars = [chr(byte ^ key) for byte, key in zip(encrypted_bytes, keys)]
        decrypted_text = "".join(decrypted_chars)
    except Exception as e:
        print(f"[!] ERROR during decryption: {e}")
        return False

    decrypted_bytes = decrypted_text.encode('utf-8')
    new_hash = hashlib.sha256(decrypted_bytes).hexdigest()

    print("[*] DECRYPTION COMPLETE. Verifying integrity...")
    if new_hash == saved_signature:
        print("\n[+] INTEGRITY VERIFIED: Hashes match perfectly. Data is authentic.")
        print(f"\n--- DECRYPTED PAYLOAD ---\n{decrypted_text}\n-------------------------")
        return True
    else:
        print("\n[!] CRITICAL WARNING: Hashes do not match. The file was tampered with!")
        return False