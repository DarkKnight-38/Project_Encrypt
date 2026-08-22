import os
import hashlib
import pickle

def min_decrypt(): #Sasank
    pass

def inter_decrypt(): #Sasank
    pass

def max_decrypt(txt_file, enc_key_file, current_uid):#Raphael #Completed
    if not os.path.exists(txt_file) or not os.path.exists(enc_key_file):
        print("[!] ERROR: Required files are missing.")
        return

    # 1. Read Ciphertext from .txt file
    with open(txt_file, 'r') as f_txt:
        hex_ciphertext = f_txt.read()
        
    # 2. Read Keys and Signature from Binary .dat file
    with open(enc_key_file, 'rb') as f_bin:
        security_payload = pickle.load(f_bin)
        
    keys = security_payload['keys']
    saved_signature = security_payload['signature']
    saved_uid = security_payload['uniqueid']

    print(f"[*] Verifying file ownership... (Current UID: {current_uid})")
    if current_uid != saved_uid:
        print(f"\n[!] ACCESS DENIED: File is watermarked to a different UID.")
        print("    You do not have authorization to decrypt this payload.")
        print("=" * 50)
        return
    
    # 3. Reverse the XOR Encryption
    encrypted_bytes = bytearray.fromhex(hex_ciphertext)
    decrypted_chars = [chr(byte ^ key) for byte, key in zip(encrypted_bytes, keys)]
    decrypted_text = "".join(decrypted_chars)
    
    # 4. Verify Integrity (Generate hash of decrypted text and compare)
    decrypted_bytes = decrypted_text.encode('utf-8')
    new_hash = hashlib.sha256(decrypted_bytes).hexdigest()
    
    print("[*] DECRYPTION COMPLETE. Verifying integrity...")
    
    if new_hash == saved_signature:
        print("\n[✓] INTEGRITY VERIFIED: Hashes match perfectly. Data is authentic.")
        print(f"\n--- DECRYPTED PAYLOAD ---\n{decrypted_text}\n-------------------------")
    else:
        print("\n[!] CRITICAL WARNING: Hashes do not match. The file was tampered with!")
