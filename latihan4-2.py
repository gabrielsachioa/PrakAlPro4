bilangan_1 = int(input("Masukkan bilangan ke-1: "))
bilangan_2 = int(input("Masukkan bilangan ke-2: "))
bilangan_3 = int(input("Masukkan bilangan ke-3: "))

def cek_digit_belakang(bilangan_1, bilangan_2, bilangan_3):
    if bilangan_1 % 10 == bilangan_2 % 10 == bilangan_3 % 10:
        return True
    elif bilangan_1 % 10 == bilangan_2 % 10 or bilangan_2 % 10 == bilangan_3 % 10 or bilangan_1 % 10 == bilangan_3 % 10:
        return True
    else:
        return False
    
print(cek_digit_belakang(bilangan_1, bilangan_2, bilangan_3))