plaintext = input("Enter text to encrypt: ")
ciphertext = ""
plaintextpos = 0
while (plaintextpos < len(plaintext)):
    plaintextchar = plaintext[plaintextpos]
    ASCIIValue = ord(plaintextchar)
    ASCIIValue = ASCIIValue - 3
    ciphertext = ciphertext + chr(ASCIIValue)
    plaintextpos = plaintextpos + 1
print(ciphertext)

#ord - returns integer representing unicode code point of character
#chr - given integer value will return character at unicode point

decrypt = input("Enter text to decrypt: ")
decryptedtext = ""
plaintextpos = 0
while (plaintextpos < len(decrypt)):
    plaintextchar = decrypt[plaintextpos]
    ASCIIValue = ord(plaintextchar)
    ASCIIValue = ASCIIValue + 3
    decryptedtext = decryptedtext + chr(ASCIIValue)
    plaintextpos = plaintextpos + 1
print(decryptedtext)
