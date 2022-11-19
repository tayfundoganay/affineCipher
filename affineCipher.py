def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m


def encrypt(text, key):
    # E = (a*x + b) % 26
    return ''.join(
        [chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])


def decrypt(cipher, key):
    # D(E) = (a^-1 * (E - b)) % 26 && mod
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])


def cryptography():
    #helloLabel['text'] = "Enter key function"
    print("Enter key function!")
    #a = key1Text.get()
    #b = key2Text.get()
    a = input("Enter First Value :  ")
    b = input("Enter Second Value :  ")
    #mod = input("Enter MOD Value : ")
    key = [int(a), int(b)]
    #keyLabel['text'] = 'Key function is {}x+{} '.format(key[0], key[1])
    print('f(x) = {}x+{} --> MOD 26'.format(key[0], key[1]))

    print('Select your operation! ')
    print(' A : Encryption \n B : Decryption ')
    operation = input(' ---> ')

    if (operation == 'A' or operation == 'a'):
        print('Enter Encryption Text')
        encrypt_text = input()
        print('Given Text : {}'.format(encrypt_text))
        print('Encrypted Text: {}'.format(encrypt(encrypt_text, key)))
    elif (operation == 'B' or operation == 'b'):
        print('Enter Decryption Text')
        decrypt_text = input()
        print('Given Text : {}'.format(decrypt_text))
        print('Decrypted Text: {}'.format(decrypt(decrypt_text, key)))
    else:
        print('Wrong Operation!')


def main():
    cryptography()



if __name__ == '__main__':
    main()

