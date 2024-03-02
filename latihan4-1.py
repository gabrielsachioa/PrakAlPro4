def cek_angka(a, b, c):
    if ((a != b and b != c and a != c) and ((a + b == c) or (b + c == a) or (a + c == b))):
        return True
    else:
        return False

print(cek_angka(1, 2, 3))
print(cek_angka(2, 2, 3))
print(cek_angka(3, 2, 3))
print(cek_angka(2, 4, 2))