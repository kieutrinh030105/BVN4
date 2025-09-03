def caesar_encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha(): 
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + k) % 26 + start)
        else:
            result += char
    return result


k = 11
plaintext = "Vo Thi Kieu Trinh"

ciphertext = caesar_encrypt(plaintext, k)

print("Plaintext : ", plaintext)
print("Ciphertext:", ciphertext)
