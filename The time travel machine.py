import datetime
import hashlib

# Generate a time-based password
current_time = datetime.datetime.now()
time_key = f"{current_time.year}-{current_time.month}-{current_time.day}-{current_time.hour}"

# Create a SHA-256 hash of the time key
password = hashlib.sha256(time_key.encode()).hexdigest()

print(f"Current password (hashed): {password}")

# Ask user for password
user_input = input("Enter the time-based password: ")

# Hash the user input for comparison
user_attempt = hashlib.sha256(user_input.encode()).hexdigest()

# Check authentication
if user_attempt == password:
    print("Access granted! You have authenticated with time-based security.")
else:
    print("Access denied. Either you're not from this time period or incorrect input.")

