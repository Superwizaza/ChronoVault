# Password Generator
import turtle
import random
import string
import time
import os

t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')

# List of Python color names
colors = ["red", "purple", "blue", "green", "yellow", "orange",
          "white", "pink", "gray"]

# Ask the user for the number of colors
number_of_colors = int(turtle.numinput("Number of colors",
                                       "How many colors do you want to see (1-9)?", 4, 1, 9))

# Ask the user for the number of sides
sides = int(turtle.numinput("Number of sides",
                            "How many sides do you want (2-13)?", 4, 2, 13))

# Ask the user for the number of repetitions
number_of_repetitions = int(turtle.numinput("Number of repetitions",
                                            "How many times do you want the pen to move around?", 100, 9, 999))

# Ask the user's name using turtle's textinput pop-up window
name = turtle.textinput("Enter your name", "Enter your name here")

# Draw a colorful spiral with the user-specified number of sides
for x in range(number_of_repetitions):
    t.pencolor(colors[x % number_of_colors])
    t.forward(x * 15 / sides + x)
    t.pendown()
    if name:  # Ensure name is not None before writing
        t.write(name, font=("Arial", int((x + 5) / 4), "bold"))
    t.left(360 / sides + 1)
    t.width(x * sides / 200)

# Check if person is secure
secret_pin = input("What is the password for this website?: ")

if secret_pin == "ZXCVBNMlkjhgfdsaQWERTYUIOP1092387456":  # Valid alphanumeric password
    print("Congratulations! You have logged into the SDA portal!")

    # Generate a random secure password using only lowercase letters
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for _ in range(5))

    # Encrypt the password
    def caesar_cipher(text, shift):
        encrypted_text = ''.join(
            chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a')) if char.isalpha() else char
            for char in text
        )
        return encrypted_text

    shift = 3
    print("Your new password is", caesar_cipher(password, shift))
    with open("secret.py", "w") as file:
        file.write(caesar_cipher(password, shift))

else:
    print("Warning: You have come to the wrong program! Unauthorized access may have serious consequences!")
    print("This program is going to close now!")

    # Exit the program
    exit()
