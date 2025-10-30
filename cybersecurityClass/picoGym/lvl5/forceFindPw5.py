# This is from https://play.picoctf.org/playlists/18?m=164

import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('cybersecurityClass\\lvl5\\level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('cybersecurityClass\\lvl5\\level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def force_find_pw():
    with open('cybersecurityClass\\lvl5\\dictionary.txt', 'r') as dict:
        for line in dict:
            pw = line.strip()
            currentline = line.strip()
            if hash_pw(pw) == correct_pw_hash:
                print(f'Password found: {pw}')
                decryption = str_xor(flag_enc.decode(), pw)
                print(f'Flag: {decryption}')
                return 
            print(f"{currentline} is not the password")
        else :
            print("Password not found in dictionary.")

force_find_pw()