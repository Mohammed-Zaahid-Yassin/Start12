def xor_encrypt_decrypt(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result
message = input("Enter the message: ")
key = int(input("Enter a numeric key (0-255): "))
encrypted = xor_encrypt_decrypt(message, key)
print("Encrypted message:", encrypted)
decrypted = xor_encrypt_decrypt(encrypted, key)
print("Decrypted message:", decrypted)
