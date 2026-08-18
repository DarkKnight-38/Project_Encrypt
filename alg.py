import secrets
def core_encrypt(raw_bytes):
    encrypted_bytes = bytearray()
    key_list = []
    for byte in raw_bytes:
        secure_shift = secrets.randbelow(256)
        key_list.append(secure_shift)
        scrambled_byte = byte ^ secure_shift