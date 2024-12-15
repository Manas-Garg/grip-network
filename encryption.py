from cryptography.fernet import Fernet

# Generate and store key securely
key = Fernet.generate_key()
fernet = Fernet(key)

# Encrypt and decrypt functions
def encrypt_data(data):
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data):
    return fernet.decrypt(encrypted_data.encode()).decode()

# Example usage
if __name__ == "__main__":
    sample_data = "sensitive_information"
    encrypted = encrypt_data(sample_data)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypt_data(encrypted))
