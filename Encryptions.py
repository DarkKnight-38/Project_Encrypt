import secrets

def min_encrypt(raw_bytes):#Sasank
    pass
def inter_encrypt(raw_bytes):#Sasank
    pass
def max_encrypt(raw_bytes):#Raphael
    encrypted_bytes = bytearray()
    key_list = []
    for byte in raw_bytes:
        secure_shift = secrets.randbelow(256)
        key_list.append(secure_shift)
        scrambled_byte = byte ^ secure_shift
        encrypted_bytes.append(scrambled_byte)
    return encrypted_bytes, key_list

