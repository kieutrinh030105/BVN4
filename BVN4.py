def caesar_encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():  # chỉ mã hóa chữ cái
            # Giữ nguyên chữ hoa / chữ thường
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + k) % 26 + start)
        else:
            # Giữ nguyên ký tự không phải chữ cái (dấu cách, dấu tiếng Việt...)
            result += char
    return result

k = 11
plaintext = "Võ Thị Kiều Trinh"

ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)
