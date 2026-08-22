import secrets
import os
import hashlib
import pickle

def min_encrypt():#Sasank
    pass
def inter_encrypt():#Sasank
    pass
def max_encrypt(text,txt_file,enc_key_file,UID):#Raphael
    text_bytes = text.encode('utf-8')
    og_hash = hashlib.sha256(text_bytes).hexdigest()
    keys=[secrets.randbelow(256) for _ in text]

    encrypted_bytes = bytearray([ord(char) ^ key for char, key in zip(text, keys)])
    hex_ciphertext = encrypted_bytes.hex()
    with open(txt_file, 'w') as f_txt:
        f_txt.write(hex_ciphertext)

    security_payload = {
        'keys': keys,
        'signature': og_hash,
        'uniqueid': UID
    }

    with open(enc_key_file, 'wb') as f_bin:
        pickle.dump(security_payload, f_bin)
        
    print(f"[*] SUCCESS: Data Encrypted.")
    print(f" > Ciphertext written to : {txt_file}")
    print(f" > Keys & Hash written to: {enc_key_file}")


