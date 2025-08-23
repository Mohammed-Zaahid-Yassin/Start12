import base64
def encode_base64(text):
    return base64.b64encode(text.encode()).decode()
def decode_base64(encoded):
    return base64.b64decode(encoded.encode()).decode()
message = input("Enter a message to encode in Base64: ")
encoded = encode_base64(message)
print("Encoded:", encoded)
decoded = decode_base64(encoded)
print("Decoded (original):", decoded)
