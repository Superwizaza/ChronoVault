# Optimized function to decrypt Caesar cipher (handles both cases)
def caesar_decipher(text, shift):
    def shift_char(char, base):
        return chr(((ord(char) - ord(base) - shift + 26) % 26) + ord(base))

    return ''.join(
        shift_char(char, 'a') if 'a' <= char <= 'z' else
        shift_char(char, 'A') if 'A' <= char <= 'Z' else char
        for char in text
    )

# Example encrypted text (assuming it was shifted forward)
encrypted_text = "Dwwdfn"
shift = 3  # Shift value used for decryption

# Print the decrypted result
decrypted_text = caesar_decipher(encrypted_text, shift)
print(f"Decrypted text: {decrypted_text}")
