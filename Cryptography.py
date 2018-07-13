alphabet = "abcdefghijklmnopqrstuvwxyz"
def main():
    original = input("Message: ")
    
    n = 1
    
    ciphertext = encrypt(n, original)
    plaintext = decrypt(n, ciphertext)
    
    print()
    print("Original message: ", original)
    print("Encoded message: ", ciphertext)
    print("Decoded message: ", plaintext)
    print()

def encrypt(n, plaintext):
    ciphertext = ""
    
    for letter in plaintext:
        ciphertext += shift(letter, n, "e")
        
    return ciphertext
    
def decrypt(n, ciphertext):
    plaintext = ""
    
    for letter in ciphertext:
        plaintext += shift(letter, n, "d")
        
    return plaintext
    
def shift(char, n, mode):
    if mode.lower().startswith("e"):
        try:
            return alphabet[(alphabet.index(char) + n) % 26]
        except ValueError:
            return char

    elif mode.lower().startswith("d"):
        try:
            return alphabet[(alphabet.index(char) - n) % 26]
        except ValueError:
            return char

    else:
        print("ERROR: Invalid mode selected")


if __name__ == "__main__":
    main()