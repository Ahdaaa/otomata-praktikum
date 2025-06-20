import re

# Reserved words dan simbol
reserved_words = {
    'if', 'else', 'for', 'while', 'return', 'int', 'float', 'double', 'char', 'void'
}
symbols = {'+', '-', '*', '/', '=', '==', '!=', '<', '>', '>=', '<=', ';', ',', '(', ')', '{', '}'}

# Fungsi klasifikasi token
def classify_token(token):
    if token in reserved_words:
        return "Reserved Word"
    elif token in symbols:
        return "Simbol / Tanda Baca"
    elif re.match(r'^[a-zA-Z_]\w*$', token):
        return "Variabel"
    elif token.isdigit():
        return "Literal Angka"
    else:
        return "Tidak Dikenali"

# Fungsi untuk mengecek apakah sebuah baris adalah ekspresi matematika
def is_math_expression(line):
    math_ops = ['+', '-', '*', '/', '=', '(', ')']
    contains_ops = any(op in line for op in math_ops)
    # abaikan baris yang dimulai dengan keyword seperti "if", "while", "return"
    starts_with_reserved = any(line.strip().startswith(rw) for rw in reserved_words)
    return contains_ops and not starts_with_reserved

# Fungsi utama: tokenisasi dan klasifikasi per baris
def tokenize_and_classify_lines(code):
    lines = code.strip().splitlines()
    all_results = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        if is_math_expression(stripped):
            all_results.append((stripped, "Kalimat Matematika"))
            continue

        # Tokenisasi biasa
        for sym in sorted(symbols, key=len, reverse=True):
            stripped = stripped.replace(sym, f' {sym} ')
        tokens = stripped.split()

        for token in tokens:
            category = classify_token(token)
            all_results.append((token, category))

    return all_results

# Contoh input
program_code = """
int result = a + b * (c - d);
if (result > 10) {
    return result;
}
"""

# Jalankan dan tampilkan hasil
tokens = tokenize_and_classify_lines(program_code)

for token, category in tokens:
    print(f"{token:30} → {category}")
