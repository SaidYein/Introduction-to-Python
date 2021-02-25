text = "Brutus is the killer!"
print(text)

shift = 1
cipher_text = ""

for char in text:
    if char.isalpha():
        if char.isupper():
            shifted_char = ord("A") + (ord(char) - ord("A") + shift)%26
        else:
            shifted_char = ord("a") + (ord(char) - ord("a") + shift)%26        
        cipher_text += chr(shifted_char)
    else:
        cipher_text += char
        
print(cipher_text)