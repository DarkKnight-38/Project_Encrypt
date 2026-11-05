import os
import secrets
import hashlib
import pickle
import random
import UI

def min_encrypt(encrypted_file, encryption_key_file, text, uid):
    UI.header("Minimum Shift Encryption", "Per-character dynamic shift cipher")
    if not text:
        UI.warning("Text to encrypt cannot be empty.")
        return

    encrypted_file = str(encrypted_file) + ('' if str(encrypted_file).endswith('.txt') else '.txt')
    encryption_key_file = str(encryption_key_file) + ('' if str(encryption_key_file).endswith('.dat') else '.dat')

    for output_file in (encrypted_file, encryption_key_file):
        if os.path.exists(output_file) and not UI.prompt_confirm(
            f"File '{output_file}' already exists. Overwrite it?", default=False
        ):
            UI.info("Encryption cancelled. No files were changed.")
            return

    keys = []
    encrypted_chars = []
    for char in text:
        shift = random.randint(-20, 20)
        keys.append(shift)
        encrypted_chars.append(chr(ord(char) + shift))

    encrypted_text = "".join(encrypted_chars)

    try:
        with open(encrypted_file, "w", encoding="utf-8") as f_txt:
            f_txt.write(encrypted_text)

        with open(encryption_key_file, "wb") as f_bin:
            pickle.dump({"keys": keys, "uniqueid": uid}, f_bin)

        UI.success("Data successfully encrypted!")
        UI.cipher_summary("Encryption", "Minimum Dynamic Shift", encrypted_file, encryption_key_file)
    except Exception as e:
        UI.error(f"Failed to write encrypted files: {e}")

def inter_encrypt(encrypted_file, encryption_key_file, text, uid):
    UI.header("Intermediate Encryption", "Vigenère polyalphabetic cipher")
    if not text:
        UI.warning("Text to encrypt cannot be empty.")
        return
    encrypted_file = str(encrypted_file) + ('' if str(encrypted_file).endswith('.txt') else '.txt')
    encryption_key_file = str(encryption_key_file) + ('' if str(encryption_key_file).endswith('.dat') else '.dat')

    for output_file in (encrypted_file, encryption_key_file):
        if os.path.exists(output_file) and not UI.prompt_confirm(
            f"File '{output_file}' already exists. Overwrite it?", default=False
        ):
            UI.info("Encryption cancelled. No files were changed.")
            return

    while True:
        key = UI.prompt_text("Enter Vigenère cipher keyword (letters only)").strip().upper()
        if not key:
            UI.warning("Cipher keyword cannot be empty.")
            continue
        if not key.isalpha():
            UI.warning("Cipher keyword must contain letters only (A-Z).")
            continue
        break

    encrypted_chars=[]

    for i in range(len(text)):
        if text[i].isalpha() and text[i].isascii():
            shift = ord(key[i % len(key)]) - ord('A')
            base = ord('A') if text[i].isupper() else ord('a')
            encrypted_chars.append(chr((ord(text[i]) - base + shift) % 26 + base))
        else:
            encrypted_chars.append(text[i])
    encrypted_text = "".join(encrypted_chars)

    try:
        with open(encrypted_file, "w", encoding="utf-8") as f_txt:
            f_txt.write(encrypted_text)
    
        with open(encryption_key_file, "wb") as f_bin:
            pickle.dump({"key": key, "keys": key, "uniqueid": uid}, f_bin)
    
        UI.success("Data successfully encrypted!")
        UI.cipher_summary("Encryption", "Intermediate Vigenère Cipher", encrypted_file, encryption_key_file)
    except Exception as e:
        UI.error(f"Failed to write encrypted files: {e}")
        

def max_encrypt(text, encrypted_file, encryption_key_file, UID):
    UI.header("Maximum XOR Stream Encryption", "Cryptographic stream cipher with SHA-256 signature")
    if not text:
        UI.warning("Text to encrypt cannot be empty.")
        return

    encrypted_file = str(encrypted_file) + ('' if str(encrypted_file).endswith('.txt') else '.txt')
    encryption_key_file = str(encryption_key_file) + ('' if str(encryption_key_file).endswith('.dat') else '.dat')

    for output_file in (encrypted_file, encryption_key_file):
        if os.path.exists(output_file) and not UI.prompt_confirm(
            f"File '{output_file}' already exists. Overwrite it?", default=False
        ):
            UI.info("Encryption cancelled. No files were changed.")
            return

    text_bytes = text.encode("utf-8")
    og_hash = hashlib.sha256(text_bytes).hexdigest()

    keys = [secrets.randbelow(256) for _ in text]
    encrypted_integers = [ord(char) ^ key for char, key in zip(text, keys)]
    hex_ciphertext = bytearray(encrypted_integers).hex()

    security_payload = {
        "keys": keys,
        "signature": og_hash,
        "uniqueid": UID
    }

    try:
        with open(encrypted_file, "w", encoding="utf-8") as f_txt:
            f_txt.write(hex_ciphertext)

        with open(encryption_key_file, "wb") as f_bin:
            pickle.dump(security_payload, f_bin)

        UI.success("Cryptographic grade encryption complete!")
        UI.cipher_summary("Encryption", "Maximum XOR Stream + SHA-256", encrypted_file, encryption_key_file, og_hash)
    except Exception as e:
        UI.error(f"Encryption failed: {e}")