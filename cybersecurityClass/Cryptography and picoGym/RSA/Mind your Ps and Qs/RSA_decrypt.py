'''
Decrypt my super sick RSA:
c: 62324783949134119159408816513334912534343517300880137691662780895409992760262021      --> This is the cipher
n: 1280678415822214057864524798453297819181910621573945477544758171055968245116423923    --> This is the public key
e: 65537                                                                                 --> This is the encryption key?

'''


c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021
n = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923
e = 65537

p = 1899107986527483535344517113948531328331
q = 674357869540600933870145899564746495319033 


def encrypt():
    message = input("What message do you want to encrypt?")
    message_ints = int.to_bytes(message, 'utf-8')
    cipher = pow(message_ints, e, n)
    print(f"This is your cipher that is encrypted:{cipher}\nThis is the public key: {n}\nThis is the encryption key: {e}\n")

def decrypt_private_key() :
    phi = (p-1) * (q-1)

    decryption_private_key = pow(e, -1, phi)

    message = pow(c, decryption_private_key, n)

    '''
    No idea what's going on after this point.
    I know it's supposed to be converting the
    number to bytes, then to plaintext, but this
    is just chatgpt coppied with some changes.
    '''

    message_bytes = message.to_bytes((message.bit_length() + 7) // 8, 'big')  # No idea especially this line😭😭

    try:
        print("As text:", message_bytes.decode('utf-8'))
    except Exception:
        pass
decrypt_private_key()