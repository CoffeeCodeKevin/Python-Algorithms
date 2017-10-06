def decrypt(encrypted_text, n):
    for i in range(n):
        half = len(encrypted_text) // 2
        decrypted = ''
        count = 0
        first = encrypted_text[0:half]
        second = encrypted_text[half:]
        while len(decrypted) < len(encrypted_text):
            if 0 <= count < len(first):
                decrypted += (second[count] + first[count])
            else:
                decrypted += second[count]
            count += 1
        encrypted_text = decrypted
    return encrypted_text

def encrypt(text, n):
    for i in range(n):
        text = (text[1::2] + text[0::2])
    return text
