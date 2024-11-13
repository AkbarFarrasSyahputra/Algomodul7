def cek_bilangan_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka)):
        if angka % i == 0:
            return False
    return True

while True:
    angka = float(input("Masukkan angka): "))
    if angka == 'Enter':
        break

    if cek_bilangan_prima(int(angka)):
        print("Adalah bilangan prima")
    else:
        print("Bukan bilangan prima")
                 
