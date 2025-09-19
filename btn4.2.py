def encrypt_z26(plaintext, k=11):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            # (P + k) mod 26
            ciphertext += chr((ord(ch) - base + k) % 26 + base)
        else:
            ciphertext += ch
    return ciphertext

P = "VoThiKieuTrinh"
print("Plaintext :", P)
C = encrypt_z26(P, 11)
print("Ciphertext:", C)