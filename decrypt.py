from cryptography.fernet import Fernet
import os

# Function to load the Fernet key
def load_key(key_path='d:/projects/Keylogger/key.key'):
    return open(key_path, 'rb').read()

# Function to decrypt text using Fernet
def decrypt_text(key, encrypted_text):
    f = Fernet(key)
    return f.decrypt(encrypted_text)

# Function to read encrypted text from file
def read_encrypted_text(filename):
    with open(filename, 'rb') as f:
        return f.readlines()

# Function to write decrypted text to file
def write_decrypted_text(filename, decrypted_text):
    with open(filename, 'wb') as f:
        f.writelines(decrypted_text)

def main():
    key_path = 'd:/projects/Keylogger/key.key'
    encrypted_file_path = 'd:/projects/Keylogger/keylogger.txt'
    decrypted_file_path = 'd:/projects/Keylogger/decrypted_keylogger.txt'

    # Load the key
    key = load_key(key_path)

    # Read the encrypted text
    encrypted_text_lines = read_encrypted_text(encrypted_file_path)

    # Decrypt the text
    decrypted_text_lines = [decrypt_text(key, line.strip() + b'\n') for line in encrypted_text_lines]

    # Write the decrypted text to a new file
    write_decrypted_text(decrypted_file_path, decrypted_text_lines)

    print(f"Decrypted text saved to {decrypted_file_path}")

if __name__ == "__main__":
    main()
