import secrets
import os
import hashlib
import pickle
import random
def min_encrypt(encrypted_file, encryption_key_file, text, uid):#Sasank
    a=''
    l=[]
    f=open(encrypted_file,'w')
    for i in text:
        k=random.randint(1,25)
        l.append(k)
        a+=chr(ord(i)+k)
    f.write(a)
    f.close()
    f=open(encryption_key_file,'wb')
    pickle.dump([l,uid],f)
    f.close()
def inter_encrypt():#Sasank
    pass
def max_encrypt(text, txt_file, enc_key_file, UID):
    encoding_format = 'utf-8'
    text_bytes = text.encode(encoding_format)
    
    hash_generator = hashlib.sha256()
    hash_generator.update(text_bytes)
    og_hash = hash_generator.hexdigest()
    
    keys = []
    text_length = len(text)
    
    for i in range(text_length):
        random_value = secrets.randbelow(256)
        keys.append(random_value)
        
    encrypted_integers = []
    index_tracker = 0
    
    for char in text:
        char_code = ord(char)
        current_key = keys[index_tracker]
        xored_value = char_code ^ current_key
        encrypted_integers.append(xored_value)
        index_tracker += 1
        
    encrypted_bytes_array = bytearray(encrypted_integers)
    hex_formatted_ciphertext = encrypted_bytes_array.hex()
    
    text_file_object = open(txt_file, 'w')
    text_file_object.write(hex_formatted_ciphertext)
    text_file_object.close()
    
    security_payload = dict()
    
    security_payload['keys'] = keys
    security_payload['signature'] = og_hash
    security_payload['uniqueid'] = UID
    
    binary_file_object = open(enc_key_file, 'wb')
    pickle.dump(security_payload, binary_file_object)
    binary_file_object.close()
    
    print()
    print("[*] SUCCESS: Data Encrypted.")
    
    output_msg_part_1 = " > Ciphertext written to : "
    final_output_1 = output_msg_part_1 + str(txt_file)
    print(final_output_1)
    
    output_msg_part_2 = " > Keys & Hash written to: "
    final_output_2 = output_msg_part_2 + str(enc_key_file)
    print(final_output_2)
    print()
