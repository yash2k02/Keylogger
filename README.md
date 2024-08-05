# Keylogger 

## Overview

This project is a keylogger designed to record keystrokes and send the recorded data via email to a specified email address. The keystrokes are encrypted for security purposes before being sent.

## Features

- **Keystroke Recording**: Records all keystrokes made by the user.
- **Encryption**: Encrypts the recorded keystrokes using the Fernet symmetric encryption method.
- **Email Sending**: Sends the encrypted keystroke data and encryption key to a specified email address.
- **Decryption**: Provides a script to decrypt the recorded keystrokes using the encryption key.

## Prerequisites

To run this project, you'll need:

- Python 3.x
- The following Python libraries:
  - pynput
  - cryptography
  - smtplib
  - email

