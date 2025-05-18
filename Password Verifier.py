# Password Verifier

# These lines of code are for encrypting the code
def caesar_decipher(text, shift):
    return ''.join(
        chr(((ord(c) - ord('a') - shift) % 26) + ord('a')) if c.isalpha() else c
        for c in text.lower()
    )

with open("secret.py") as f:
    encrypted = f.read().strip()

password = input("WHat is the password for this portal?")
shift = 3  # Set this to the shift you used when encrypting the password
decrypted_password = caesar_decipher(encrypted, shift)

#Checking if user is reliable or not
if password == decrypted_password:
    print("Congratulations for logging into the SDA portal!")

else:
    print("You are not authorized to access this page! Leave immediately or serious allegations may be put on you!") 
    
    # Exit the program
    exit()
