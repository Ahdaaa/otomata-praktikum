def is_palindrome(s: str) -> bool:
    """
    Fungsi untuk mengecek apakah suatu string merupakan palindrome.
    Parameter:
        s (str): String input
    Return:
        bool: True jika palindrome, False jika tidak
    """
    return s == s[::-1]  # Membandingkan string dengan versi terbaliknya


def main():
    # Himpunan input string (kombinasi huruf dan angka)
    input_strings = [
        'x1y2y1x',
        '7a8b8a7',
        'r4t5t4r',
        'm9n8o8n9m',
        'b2c3d3c2b',
        'hello123',
        'q9w8e8w9q'
    ]

    # Mengambil hanya string yang merupakan palindrome
    palindrome_strings = [s for s in input_strings if is_palindrome(s)]

    # Menampilkan hasil
    print("📌 String-string palindrome yang ditemukan:")
    for i, s in enumerate(palindrome_strings, start=1):
        print(f"{i}. {s}")


if __name__ == "__main__":
    main()
