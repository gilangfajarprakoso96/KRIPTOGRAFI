def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:  # decrypt
                new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    return result

def main():
    while True:
        mode = input("Pilih mode (enkripsi/dekripsi) atau 'keluar' untuk mengakhiri: ").lower()
        if mode == 'keluar':
            break
        elif mode not in ['enkripsi', 'dekripsi']:
            print("Mode tidak valid. Silakan pilih 'enkripsi' atau 'dekripsi'.")
            continue

        text = input("Masukkan teks: ")
        shift = int(input("Masukkan jumlah pergeseran (1-25): "))

        if mode == 'enkripsi':
            result = caesar_cipher(text, shift, 'encrypt')
            print(f"Hasil enkripsi: {result}")
        else:
            result = caesar_cipher(text, shift, 'decrypt')
            print(f"Hasil dekripsi: {result}")

if __name__ == "__main__":
    main()
