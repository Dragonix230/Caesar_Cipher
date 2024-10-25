# Caesar Cipher Encryption and Decryption
def encrypt(text, shift):
    result = ""
    for i in text:
        if i.isupper():  # Encrypt uppercase characters
            result += chr((ord(i) + shift - 65) % 26 + 65)
        elif i.islower():  # Encrypt lowercase characters
            result += chr((ord(i) + shift - 97) % 26 + 97)
        else:
            result += i  # Keep spaces and punctuation unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Do you want to Encrypt or Decrypt? (E/D): ").upper()
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        print("Encrypted message:", encrypt(text, shift))
    elif choice == 'D':
        print("Decrypted message:", decrypt(text, shift))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
