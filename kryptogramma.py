def calculate_key(message_len, key):
    full_key = ""

    while len(full_key) <= message_len:
        full_key += key + key[::-1]

    return full_key[:message_len]

def encrypt(txt_message,key):
    full_key = calculate_key(len(txt_message), key)
    encrypted_message = []

    for digit in range(0, len(txt_message)):
        n1 = ord(txt_message[digit])
        n2 = ord(full_key[digit])
        encrypted_message.append(2*n1+3*n2)

    return encrypted_message

def  decrypt(encrypted_message,key):
    full_key = calculate_key(len(encrypted_message), key)
    decrypted_message = ""

    for digit in range(0, len(encrypted_message)):
        enc = encrypted_message[digit]
        p = ord(full_key[digit])
        dec = int((enc-(3*p))/2)
        decrypted_message += chr(dec)

    return decrypted_message

def main():
    txt_message = input("Dwse to mhnyma pros kryptografhsh: ")
    key = input("Dwse to kleidi ths kryptografhshs: ")
    full_key = calculate_key(len(txt_message), key)
    encrypted_message = encrypt(txt_message, key)
    decrypted_message = decrypt(encrypted_message, key)
    print(f"\n{txt_message}")
    print(f"{full_key}")
    print(f"\nKryptografhmeno mhnyma: \n{encrypted_message}")
    print(f"\nApokryptografhmeno mhnyma: \n{decrypted_message}")

if __name__ == '__main__':
    main()

