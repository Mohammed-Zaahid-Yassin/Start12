import random
import string

def generate_password(length):
    # Combine letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the length of the password: "))
print("Your password is:", generate_password(length))
