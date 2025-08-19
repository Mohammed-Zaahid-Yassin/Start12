def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted
message = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value (e.g., 3): "))
encrypted_message = caesar_encrypt(message, shift)
print("Encrypted message:", encrypted_message)
