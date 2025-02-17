import streamlit as st
import pyperclip  # For copy-to-clipboard functionality

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

# Streamlit App
def main():
    # Set app title and description
    st.title("Caesar Cipher App")
    st.write("A simple app to encrypt or decrypt messages using the Caesar Cipher.")

    # User inputs
    choice = st.radio("Choose an action:", ("Encrypt", "Decrypt"))
    text = st.text_area("Enter your message:")
    
    # Shift value input with dropdown for predefined values
    shift_options = list(range(0, 101))  # Supports shift values from 0 to 100
    shift = st.selectbox("Select or enter the shift value:", shift_options, index=3)

    # Process the input
    if st.button("Process"):
        if not text:
            st.warning("Please enter a message.")
        else:
            if choice == "Encrypt":
                result = encrypt(text, shift)
                st.success(f"Encrypted message: {result}")
            else:
                result = decrypt(text, shift)
                st.success(f"Decrypted message: {result}")

            # Copy-to-clipboard button
            if st.button("Copy to Clipboard"):
                pyperclip.copy(result)
                st.info("Result copied to clipboard!")

if __name__ == "__main__":
    main()
