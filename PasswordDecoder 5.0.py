# PasswordDecoder 5.0.py

# These lines of code are for encrypting the code
def caesar_decipher(text, shift):
    return ''.join(
        chr(((ord(c) - ord('a') - shift) % 26) + ord('a')) if c.isalpha() else c
        for c in text.lower()
    )

with open("secret.py") as f:
    encrypted = f.read().strip()

# Print the result
print("Decrypted word:", caesar_decipher(encrypted, 3))
