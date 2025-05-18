import string
import os  

# Define the attack password
attack = "attack"  # Now "attack" is the correct password

# Ask for the password
other_password = input("What is the password for this database? ")

if other_password == attack:
    print("Congratulations for logging into the SDA portal!!!")
    # Delete the secret file for security reasons after access
    os.remove("secret.py")
else:
    print("You have come to the wrong program or have the wrong password.")
    print("Unauthorized access may result in serious consequences.")
