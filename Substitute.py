import random

alphabet = "abcdefghijklmnopqrstuvwxyz"


def main():
    key = make_key(alphabet)
    
    original = input("Message: ").lower()
    ciphertext = encrypt(original, key)
    plaintext = decrypt(ciphertext, key)

    print()
    print("Original text: ", original)
    print("Encrypted text:", ciphertext)
    print("Decrypted text:", plaintext)
    print()
    
def encrypt(text, key):
    
def decrypt(text, key):
    
def make_key(alphabet):
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    return ''.join(shuffled)


if __name__ == "__main__":
    main()