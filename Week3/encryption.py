# Encryption program
plaintext= input("Enter text to encrypt: ")
ciphertext = ("")
alphabet  = ("XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC")
plaintextpos = 0
while (plaintextpos < len(plaintext)):
        plaintextchar = plaintext[plaintextpos]
        alphabetpos = 3
        while (plaintextchar != alphabet[alphabetpos]):
            alphabetpos = alphabetpos + 1
        alphabetpos = alphabetpos - 3
        ciphertext = ciphertext + alphabet[alphabetpos]
        plaintextpos = plaintextpos + 1
print(ciphertext)


# Decryption prorgam
decrypt = input("Enter text to decrypt: ")
decryptedtext = ""
plaintextpos = 0
while (plaintextpos < len(decrypt)):
        plaintextchar = decrypt[plaintextpos]
        alphabetpos = 0
        while (plaintextchar != alphabet[alphabetpos]):
            alphabetpos = alphabetpos + 1
        alphabetpos = alphabetpos + 3
        decryptedtext = decryptedtext + alphabet[alphabetpos]
        plaintextpos = plaintextpos + 1
print(decryptedtext)
