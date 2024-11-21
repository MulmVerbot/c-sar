def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
    
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

if __name__ == "__main__":
    mode = input("Modus (encrypt/decrypt): ").strip().lower()
    text = input("Gib den Text ein: ")
    shift = int(input("Verschiebung (Schlüssel): "))
    
    output = caesar_cipher(text, shift, mode)
    print(f"Ergebnis: {output}")
